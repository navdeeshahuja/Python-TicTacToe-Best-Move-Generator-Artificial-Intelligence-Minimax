import TicTacToeMaster as ttt

board, nextMove = ttt.getRandomBoard()
print(board)
ttt.printBoard(board)
bestMove = ttt.getAIMove(board, nextMove, nextMove)
print(nextMove+" should play at: " + str(bestMove[0]) + " index")
