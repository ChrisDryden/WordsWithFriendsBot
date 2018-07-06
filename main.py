import client_wwf as WWF
from ExternalLibraries.fiend import Fiend

username = 'redacted'
password = 'redacted'

def initial_main():
	session = WWF.login(username, password)
	data = WWF.get_games(session)
	for item in data:
		#print("There is a current game against: " + str(data['id']))
		board  = WWF.build_board(item)
		print(board)
		print(item)


def fiend_main():
	game = Fiend(username, password)
	#print(game.games)
	active_games = game.activeGames

	for gameID in active_games:
		#print(active_games[gameID])
		#print(active_games[gameID].letterBagCodes)
		#print(active_games[gameID].remainingLetters)
		#print(active_games[gameID].remainingLetters)
		print('game:')
		print(active_games[gameID].opponent.rackLetters)
		print(active_games[gameID].creator.rackLetters)




fiend_main()