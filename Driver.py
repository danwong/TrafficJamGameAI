import TrafficJam as TJ

def main():
   board = TJ.initializeBoard()
   TJ.printBoard(board)
   result = TJ.move(board, 6)
   print(result[1])



if __name__ == "__main__":
   main()
