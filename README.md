# Python TicTacToe Best Move Generator

A Python script to generate the best move for the TicTacToe Game.
Uses the Backtracking technique to make unbeatable moves.
Feel free to make changes :) 

## Demo
```	python
	>>> import TicTacToeMaster as ttt

	>>>  board, nextMove = ttt.getRandomBoard()
	>>> ttt.printBoard(board)
	>>>
	_   _   _   
	O   X   _   
	O   O   X   

	>>> bestMove = ttt.getAIMove(board, nextMove, nextMove)
	>>> print(nextMove+" should play at: " + str(bestMove[0]) + " index")
	>>> 
	X should play at: 0 index

	>>> board = [" ", " ", "X", " ", "O", " ", "X", " ", " "]
    >>> bestMovePosition = ttt.getAIMove(board, "O", "O")[0]
    >>> print("O should play at: " + str(bestMovePosition) + " index")
    >>> 
	O should play at: 1 index

```

## Installation

Just Copy the TicTacToeMaster.py in your project and you are good to go

## Dependencies

None, pure python code.

## Usage
``` python
    import TicTacToeMaster as ttt

    board = [" ", " ", "X", " ", "O", " ", "X", " ", " "]
	ttt.printBoard(board)
	aiPlayer = "O"
	bestMove = ttt.getAIMove(board, aiPlayer, aiPlayer)
	bestPosition = str(bestMove[0])
	print(aiPlayer + " should play at " + bestPosition + " index")
```

## Unbeatable Bot
``` python
	
	>>> 
	Where do you want to play X: 7


	_   _   _   
	_   O   _   
	X   _   _   

	Where do you want to play X: 3


	_   O   X   
	_   O   _   
	X   _   _   

	Where do you want to play X: 8


	_   O   X   
	_   O   _   
	X   X   O   

	Where do you want to play X: 1


	X   O   X   
	O   O   _   
	X   X   O   

	Where do you want to play X: 6


	X   O   X   
	O   O   X   
	X   X   O   

```

## License
MIT License

Copyright (c) 2017 Navdeesh Ahuja

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.