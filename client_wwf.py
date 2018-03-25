"""
 Simple bot to log into and play WWF
"""
from requests import Session
import json


"""
TODO
make this actually behave like a client!

get games
for each game
- get letters
- get board state
- make valid move
get challenges
for each challenge
- get letters
- get board state
- make valid move

# something like this
s = login(username, password)
data = get_user_data(s)
games = get_games(s)
for game in games:
    letters = get_letters(s, game)
    state = get_board_state(s, game)
    move = get_next_move(letters, state)
    make_move(s, move)
"""


HOST = 'https://wordswithfriends.zyngawithfriends.com'
BUNDLE_NAME = 'WordsWithFriends3'
CLIENT_VERSION = '10.26'

MAX_ACTIVE = 0
BLACKLIST = []
WHITELIST = []

WWF_TILE_IDS = {chr(n): set() for n in range(ord('A'), ord('Z') + 1)}
WWF_TILES = [None for _ in range(105)]
BOARD_SIZE = 15


def _log_request_status(r, *args, **kwargs):
    parts = [r.status_code, r.request.method, r.request.url]
    if r.request.body:
        parts.append(r.request.body)
    print(*parts)

    if not r.ok:
        parts.append(r.text)
        raise ValueError('Request Failed: ', *parts)


def get_initial_config():
    s = Session()

    s.hooks['response'].append(_log_request_status)
    s.headers.update({'Accept': 'application/json'})

    url = '/jumps/config'
    query = {
        'bundle_name': BUNDLE_NAME,
        'client_version': CLIENT_VERSION,
        'plaintext': 1,
    }

    # initial config
    r = s.get(HOST + url, params=query)
    d = json.loads(r.text)
    MAXACTIVE = int(d['MaxActiveGamesForCreate'])
    BLACKLIST.extend(d['BlackListedWords'].split(','))
    WHITELIST.extend(d['WhiteListedWords'].split(','))
    return s


def login(login, password):
    s = get_initial_config()
    url = '/sessions/create'
    data = {
        'login_request': {'login': login, 'password': password}
    }
    s.post(HOST + url, json=data)
    return s


def get_user_data(s):
    url = '/user_data'
    params = {
        'badges': True,
        'game_type': 'WordGame',
        'include_item_data': True
    }
    r = s.get(HOST + url, params=params)
    d = json.loads(r.text)
    return r


def get_games(s):
    url = '/games'
    params = {
        'game_type': 'WordGame',
        'get_current_user': True,
        'include_invitations': True,
        'include_item_data': True,
        'chat_messages_since': 0,
        'moves_since': 0
    }
    r = s.get(HOST + url, params=params)
    d = json.loads(r.text)
    return d['games']


def build_board(g):
    board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    moves = g['moves']
    for m in moves:
        if m['move_type'] != 'play' or not m['text'] or not m['words']:
            continue

        word = m['words'][0].upper()
        x = m['from_x']
        y = m['from_y']
        text = m['text'].split(',')[:-1]

        is_horizontal = m['from_y'] == m['to_y']
        i = 0
        for c in text:
            # '76,47,5,18,67,1,e,48,' == GREASER
            # '42,8,*,31,' == MEAL

            if not c.isdigit() and c is not '*':
                continue

            board[y][x] = word[i]
            if c != '*':
                WWF_TILE_IDS[word[i]].add(int(c))
                WWF_TILES[int(c)] = word[i]

            if is_horizontal:
                x += 1
            else:
                y += 1

            i += 1
    return board


def board_to_str(board):
    b = '  ' + '|'.join(map(str, [i % 10 for i in range(BOARD_SIZE)]))
    i = 0
    for row in board:
        b += '\n' + str(i % 10) + ' ' + '|'.join(row)
        i += 1
    return b


def game_is_valid(game):
    #for u in game['users']:
    #    if type(u['id']) is list and 25505715 in u['id']:
    #        return false
    return True  #game['days_left'] > 0


def get_tiles(s, game):
    print(game['id'])
    print([n['name'] for n in game['users']])
    pass


def get_next_move(letters, state):
    pass


def make_move(s, move):
    url = '/moves'
    params = {
        'points': 69,
        'words': ['BLAH', 'ALAMO']
    }
    pass


def get_chat_messages(s, user):
    pass


def get_daily_drip(s):
    url = '/packages/grant_daily_drip'
    return s.get(HOST + url)