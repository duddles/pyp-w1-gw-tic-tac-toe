
# exceptions
class InvalidMovement(Exception):
    pass


class GameOver(Exception):
    pass


# internal helpers
def _position_is_empty_in_board(position, board):
    pass


def _position_is_valid(position):
    pass


def _board_is_full(board):
    pass


def _is_winning_combination(board, combination, player):
    pass


def _check_winning_combinations(board, player):
    pass


# public interface
def start_new_game(player1, player2):
    pass


def get_winner(game):
    pass


def move(game, player, position):
    pass


def get_board_as_string(game):
    pass


def get_next_turn(game):
    pass
