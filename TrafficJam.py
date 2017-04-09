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

#returns boolean, important for keeping track of rewards for neural network
#If a move was False because of an index error, we will need to make sure the board does 
#not update. Therefore, the board should be copied into another temp variable so if this returns as false, then

##### Either return a tuple including the boolean and updated/notupdated list or list of the two return values
#do not update
def move(board, input):
   left = '<'
   right = '>'
   initialBoard = board
   try:
      #If the index is a left move
      if (board[input] == left):
         #If the index to the left of the left move is empty, move left
         if board[input-1] == ' ':
            board[input] = ' ' #Empty out index and move
            board[input-1] = '<'
            return ['T', board]
         #If the index to the left of the left move is a right, hop.
         elif board[input-1] == right:
            if board[input-2] == ' ': #if two left of index is empty, replace empty with left
               board[input] = ' '
               board[input-2] = '<'
               return ['T', board]
         return ['F', initialBoard]
      elif (board[input] == right):
         #If the index to the left of the left move is empty, move left
         if board[input+1] == ' ':
            board[input] = ' ' #Empty out index and move
            board[input+1] = '>'
            return ['T', board]
         #If the index to the left of the left move is a right, hop.
         elif board[input+1] == left:
            if board[input+2] == ' ': #if two left of index is empty, replace empty with left
               board[input] = ' '
               board[input-2] = '>'
               return ['T', board]
         return ['F', initialBoard]
      #else if (board[input] == right)
      else:
         return ['F', initialBoard]

   except IndexError:
      return ['F', initialBoard]
