# -*- coding: utf-8 -*-
import unittest

from main import (start_new_game, is_valid, is_empty, is_board_complete,
                  check_win, move, print_winner, InvalidMovement, print_board,
                  is_board_complete)


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.x = "X"
        self.o = "O"
        self.game = start_new_game(self.x, self.o)

    def test_start_new_game(self):
        game = start_new_game(self.x, self.o)
        expected = {
            'player1': self.x,
            'player2': self.o,
            'board': [
                ["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"],
            ],
            'next_turn': self.x,
            'winner': None
        }
        self.assertEqual(game, expected)

    def test_is_valid_position(self):
        valid_positions = [
            (0,0), (0,1), (0,2),
            (1,0), (1,1), (1,2),
            (2,0), (2,1), (2,2),
        ]
        for position in valid_positions:
            self.assertTrue(is_valid(position))

    def test_is_valid_position_invalid(self):
        invalid_positions = [
            (2,3), (3,2), (3,3), (9,9), (-1,-1), 1, "something", False, (0,0,0)
        ]
        for position in invalid_positions:
            self.assertFalse(is_valid(position))

    def test_is_empty_position(self):
        board = self.game['board']
        empty_positions = [
            (0,0), (0,1), (0,2),
            (1,0), (1,1), (1,2),
            (2,0), (2,1), (2,2),
        ]
        for position in empty_positions:
            self.assertTrue(is_empty(position, board))
        board[0][1] = self.x
        self.assertFalse(is_empty((0,1), board))


    def test_is_board_complete(self):
        self.game['board'] = [
            ["X", "O", "O"],
            ["O", "X", "X"],
            ["O", "X", "O"],
        ]
        self.assertTrue(is_board_complete(self.game['board']))

    def test_is_board_complete_false(self):
        self.game['board'] = [
            ["X", "O", "O"],
            ["O", "-", "-"],
            ["O", "X", "O"],
        ]
        self.assertFalse(is_board_complete(self.game['board']))

    def test_check_win_no_winner(self):
        board = [
            ["X", "O", "O"],
            ["O", "X", "X"],
            ["O", "X", "O"],
        ]
        self.assertEqual(check_win(board, self.x), None)

    def test_check_win_X_wins(self):
        # diagonals
        board = [
            ["X", "O", "O"],
            ["O", "X", "X"],
            ["O", "O", "X"],
        ]
        self.assertEqual(check_win(board, self.x), "X")
        board = [
            ["O", "O", "X"],
            ["O", "X", "X"],
            ["X", "O", "O"],
        ]
        self.assertEqual(check_win(board, self.x), "X")
        # horizontals
        board = [
            ["X", "X", "X"],
            ["X", "O", "O"],
            ["O", "O", "X"],
        ]
        self.assertEqual(check_win(board, self.x), "X")
        board = [
            ["X", "O", "O"],
            ["X", "X", "X"],
            ["O", "O", "X"],
        ]
        self.assertEqual(check_win(board, self.x), "X")
        board = [
            ["X", "O", "O"],
            ["O", "O", "X"],
            ["X", "X", "X"],
        ]
        self.assertEqual(check_win(board, self.x), "X")
        # verticals
        board = [
            ["X", "O", "X"],
            ["O", "O", "X"],
            ["O", "X", "X"],
        ]
        self.assertEqual(check_win(board, self.x), "X")
        board = [
            ["X", "X", "O"],
            ["O", "X", "O"],
            ["O", "X", "X"],
        ]
        self.assertEqual(check_win(board, self.x), "X")
        board = [
            ["X", "X", "O"],
            ["X", "O", "O"],
            ["X", "O", "X"],
        ]
        self.assertEqual(check_win(board, self.x), "X")

    def test_check_win_O_wins(self):
        # diagonals
        board = [
            ["O", "X", "X"],
            ["X", "O", "O"],
            ["X", "X", "O"],
        ]
        self.assertEqual(check_win(board, self.o), "O")
        board = [
            ["X", "X", "O"],
            ["X", "O", "O"],
            ["O", "X", "X"],
        ]
        self.assertEqual(check_win(board, self.o), "O")
        # horizontals
        board = [
            ["O", "O", "O"],
            ["O", "X", "X"],
            ["X", "X", "O"],
        ]
        self.assertEqual(check_win(board, self.o), "O")
        board = [
            ["O", "X", "X"],
            ["O", "O", "O"],
            ["X", "X", "O"],
        ]
        self.assertEqual(check_win(board, self.o), "O")
        board = [
            ["O", "X", "X"],
            ["X", "X", "O"],
            ["O", "O", "O"],
        ]
        self.assertEqual(check_win(board, self.o), "O")
        # verticals
        board = [
            ["O", "X", "O"],
            ["X", "X", "O"],
            ["X", "O", "O"],
        ]
        self.assertEqual(check_win(board, self.o), "O")
        board = [
            ["O", "O", "X"],
            ["X", "O", "X"],
            ["X", "O", "O"],
        ]
        self.assertEqual(check_win(board, self.o), "O")
        board = [
            ["O", "O", "X"],
            ["O", "X", "X"],
            ["O", "X", "O"],
        ]
        self.assertEqual(check_win(board, self.o), "O")

    def test_play_no_winner(self):
        # [
        #     ["X", "O", "X"],
        #     ["O", "O", "X"],
        #     ["X", "X", "O"],
        # ]
        move(self.game, self.x, position=(0, 0))
        move(self.game, self.o, position=(0, 1))
        move(self.game, self.x, position=(0, 2))
        move(self.game, self.o, position=(1, 0))
        move(self.game, self.x, position=(1, 2))
        move(self.game, self.o, position=(1, 1))
        move(self.game, self.x, position=(2, 0))
        move(self.game, self.o, position=(2, 2))
        move(self.game, self.x, position=(2, 1))
        self.assertEqual(print_winner(self.game), None)
        self.assertTrue(is_board_complete(self.game['board']))
        with self.assertRaisesRegexp(InvalidMovement,
                                     'Game is over, no winner.'):
            move(self.game, self.o, position=(0, 0))

    def test_play_X_wins(self):
        # [
        #     ["X", "X", "X"],  <--- "X" wins
        #     ["O", "O", "-"],
        #     ["-", "-", "-"],
        # ]
        move(self.game, self.x, position=(0, 0))
        move(self.game, self.o, position=(1, 0))
        move(self.game, self.x, position=(0, 1))
        move(self.game, self.o, position=(1, 1))
        move(self.game, self.x, position=(0, 2))
        self.assertEqual(print_winner(self.game), self.x)
        with self.assertRaisesRegexp(InvalidMovement,
                                     'Game is over, "X" wins.'):
            move(self.game, self.o, position=(2, 2))

    def test_play_O_wins(self):
        # [
        #     ["O", "X", "X"],
        #     ["X", "O", "-"],
        #     ["-", "-", "O"],   <--- "O" wins
        # ]
        move(self.game, self.x, position=(0, 1))
        move(self.game, self.o, position=(0, 0))
        move(self.game, self.x, position=(0, 2))
        move(self.game, self.o, position=(1, 1))
        move(self.game, self.x, position=(1, 0))
        move(self.game, self.o, position=(2, 2))
        self.assertEqual(print_winner(self.game), self.o)
        with self.assertRaisesRegexp(InvalidMovement,
                                     'Game is over, "O" wins.'):
            move(self.game, self.x, position=(2, 0))

    def test_play_one_player_moves_twice(self):
        move(self.game, self.x, position=(0, 1))
        with self.assertRaisesRegexp(InvalidMovement, '"O" moves next'):
            move(self.game, self.x, position=(0, 0))

    def test_play_invalid_position(self):
        with self.assertRaisesRegexp(InvalidMovement,
                                     'Position out of range.'):
            move(self.game, self.x, position=(9, 8))

    def test_play_position_already_taken(self):
        move(self.game, self.x, position=(0, 0))
        with self.assertRaisesRegexp(InvalidMovement,
                                     'Position already taken.'):
            move(self.game, self.o, position=(0, 0))

    def test_print_board(self):
        self.game['board'] = [
            ["O", "O", "X"],
            ["O", "X", "X"],
            ["O", "X", "O"],
        ]
        expected = """
O  |  O  |  X
--------------
O  |  X  |  X
--------------
O  |  X  |  O
"""
        self.assertEqual(print_board(self.game), expected)
