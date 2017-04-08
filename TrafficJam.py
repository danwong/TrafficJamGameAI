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

def move(board, input):
	left = '<'
	right = '>'
	if (input == left):
		if (board[input-1] == ' '):
			board[input] = ' '
			board[input-1] = '<'
			return True
		else if (board[input-1] == '>'):
			if board[input-2] == ' '
				board[input-2] = '<'
			return True
		return False
	else if (input == right):
		

