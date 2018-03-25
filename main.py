import client_wwf as WWF

username = 'test'
password = 'test'

def main():
	session = WWF.login(username, password)
	data = WWF.get_games(session)
	for item in data:
		#print("There is a current game against: " + str(data['id']))
		board  = WWF.build_board(item)
		print(board)
		print(item)


main()