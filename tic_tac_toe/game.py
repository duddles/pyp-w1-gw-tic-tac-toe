import os
from .exceptions import InvalidMovement, GameOver

# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    return board[position[0]][position[1]] == '-'


def _position_is_valid(position):
    """
    Checks if given position is a valid. To consider a position as valid, it
    must be a two-elements tuple, containing values from 0 to 2.
    Examples of valid positions: (0,0), (1,0)
    Examples of invalid positions: (0,0,1), (9,8), False

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)

    Returns True if given position is valid, False otherwise.
    """
    if type(position) != tuple or len(position) != 2:
        return False
    return 0 <= position[0] < 3 and 0 <= position[1] < 3

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    return all(['-' not in row for row in board])

def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    for position in combination:
        if board[position[0]][position[1]] != player:
            return False
    return True

def _check_winning_combinations(board, player):
    """
    There are 8 posible combinations (3 horizontals, 3, verticals and 2 diagonals)
    to win the Tic-tac-toe game.
    This helper loops through all these combinations and checks if any of them
    belongs to the given player.

    :param board: Game board.
    :param player: One of the two playing players.

    Returns the player (winner) of any of the winning combinations is completed
    by given player, or None otherwise.
    """
    # Define all possible combinations for winning the game
    combinations = [
        ((0, 0), (0, 1), (0, 2)), # horizontals 
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)), # verticals
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)), # diagonals
        ((0, 2), (1, 1), (2, 0))
    ]

    for combination in combinations:
        if _is_winning_combination(board, combination, player):
            return player
    return None

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    board = [['-']*3 for _ in range(3)]
    game = {
        'player1': player1,
        'player2': player2,
        'board': board,
        'next_turn': player1,
        'winner': None
    }
    
    return game

def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    for player in [game['player1'], game['player2']]:
        if _check_winning_combinations(game['board'], player):
            return player
    return None

def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    # check if game is already over
    if game['winner'] or _board_is_full(game['board']):
        raise InvalidMovement('Game is over.')
    
    # check if an illegal movement is being attempted
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
    if game['next_turn'] != player:
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn']))
    
    # the move is valid so add either an 'X' or 'O' to the game board
    game['board'][position[0]][position[1]] = player
    
    # see if it was a winning move, or if it is a tie (board is full)
    winner = get_winner(game)
    if winner:
        game['winner'] = winner
        raise GameOver('"{}" wins!'.format(winner))
    if _board_is_full(game['board']):
        raise GameOver('Game is tied!')
        
    # give the next player a turn
    swap_players = {'X': 'O', 'O': 'X'}
    game['next_turn'] = swap_players[player]
    return 

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    entry_sep = '  |  '
    row_sep = '--------------'
    rows = []
    
    # format each row of the game board
    for row in game['board']:
        row_string = entry_sep.join(row)
        rows.append(row_string)
    
    # add row separators and newlines for pretty board printing
    rows.insert(3, '')
    rows.insert(2, row_sep)
    rows.insert(1, row_sep)
    rows.insert(0, '')
    return os.linesep.join(rows)

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    # If there is a winner or a tie, return None
    if game['winner'] or _board_is_full(game['board']):
        return None
    return game['next_turn']
