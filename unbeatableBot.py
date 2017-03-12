import TicTacToeMaster as ttt

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

while(not (ttt.checkWin(board, "O") or ttt.checkLose(board, "O") or ttt.checkTie(board))):
    playerPosition = int(input("Where do you want to play X: ")) - 1
    board[playerPosition] = "X"
    aiMovePosition = int(ttt.getAIMove(board, "O", "O")[0])
    board[aiMovePosition] = "O"
    ttt.printBoard(board)
