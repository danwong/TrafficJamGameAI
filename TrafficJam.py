#Daniel Wong


def initializeBoard():
	return ['>','>','>','>','>',' ', '<', '<', '<', '<', '<']

def printBoard(board):
	result = ""
	for i in board:
		result += i + " "
	print(result)

def isFinished(board):
	if board == ['<', '<', '<', '<', '<', ' ', '>', '>', '>', '>', '>']:
		return True
	return False