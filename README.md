# [pyp-w1] Tic-tac-toe

You will need to build a simple version of the classic Tic-tac-toe game.
Your program is supposed to work in a two-players basis. "Machine-mode" is not required to be implemented.

The board structure should look something similar to this:
```python
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

Once your new game configuration is done, both players can start with their movements:

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

If at some point during the game you want to check which is the current state of the board, you can invoke the `print_board` function:

```python
>>> print_board(game)
X  |  O  |  X
--------------
O  |  O  |  X
--------------
X  |  -  |  -
```

When you are reaching the final movements, there are two possible game endings: one of the players wins the game, or the game is tied:

```python
# Option 1: "O" wins the game
>>> move(game, player2, position=(2, 1))
>>> print_winner(game)
"O"
>>> move(game, player1, position=(2, 2))
InvalidMovement: Game is over, "O" wins.

# Option 2: No winner
>>> move(game, player2, position=(2, 2))
>>> move(game, player1, position=(2, 1))
>>> print_winner(game)
None
>>> move(game, player2, position=(0, 0))
InvalidMovement: Game is over, no winner.
```
