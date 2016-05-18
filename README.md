# [pyp-w1] Tic-tac-toe

You will need to build a simple version of the classic Tic-tac-toe game.
Your program is supposed to work in a two-players basis. "Machine-mode" is not required to be implemented.

The board should be implemented using nested lists. This is an example of the board:
```python
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]
```

The position of a particular cell in the board is going to be given by two indexes (first idx for the row, and second idx for the column), here's an example:

```
(0,0) | (0,1) | (0,2)
---------------------
(1,0) | (1,1) | (1,2)
---------------------
(2,0) | (2,1) | (2,2)
```

To create a new game and start doing your movements, you must follow this logic:

```python
>>> player1 = "X"
>>> player2 = "O"
>>> game = start_new_game(player1, player2)
{
    'player1': "X",
    'player2': "O",
    'board': [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ],
    'next_turn': "X",
    'winner': None
}
```

The `start_new_game` function creates a new game configuration. It will basically create a data structure (dict in this case), holding all the needed information to start playing.

Once your new game configuration is done, both players can start with their movements. To create a movement, you need to implement the `move` function, which receives three parameters: the game structure (as seen above), the player to play, and a tuple containing the position (first value for row, second for column):

```python
# Start playing...
>>> move(game, player1, position=(0, 0))
>>> move(game, player2, position=(0, 1))

# Possible errors
>>> move(game, player2, position=(0, 2))
InvalidMovement: "X" moves next.
>>> move(game, player1, position=(0, 0))
InvalidMovement: Position already taken.
>>> move(game, player1, position=(9, 9))
InvalidMovement: Position out of range.

>>> move(game, player1, position=(0, 2))
>>> move(game, player2, position=(1, 0))
>>> move(game, player1, position=(1, 2))
>>> move(game, player2, position=(1, 1))
>>> move(game, player1, position=(2, 0))
```

If at some point during the game you want to check which is the current state of the board, you can invoke the `get_board_as_string` function:

```
>>> get_board_as_string(game)
X  |  O  |  X
--------------
O  |  O  |  X
--------------
X  |  -  |  -
```

When you are reaching the final movements, there are two possible game endings: one of the players wins the game, or the game is tied. In any of the cases, a `GameOver`
exception will be raised when the last movement is performed.

```python
# Option 1: "O" wins the game
>>> move(game, player2, position=(2, 1))
GameOver: "O" wins!
>>> get_winner(game)
"O"
>>> move(game, player1, position=(2, 2))
InvalidMovement: Game is over.

# Option 2: No winner
>>> move(game, player2, position=(2, 2))
>>> move(game, player1, position=(2, 1))
GameOver: Game is tied!
>>> get_winner(game)
None
>>> move(game, player2, position=(0, 0))
InvalidMovement: Game is over.
```

As a quick summary, this is the public interface you must respect:

```python
start_new_game(player1, player2)

move(game, player, position)

get_next_turn(game)

get_board_as_string(game)

get_winner(game)
```

You will notice in the file `main.py` that some other internal helpers must
also be implemented in order to support the game.
