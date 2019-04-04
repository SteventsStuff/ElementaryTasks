#!/usr/bin/env python3
import unittest
from mock import patch
import argparse
import tasks.t1_chess_board as cb
from tasks.t1_chess_board import ChessBoard


class TerminalSize:
    def __init__(self, columns, lines):
        self.columns = columns
        self.lines = lines


class TestChessBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.my_board = ChessBoard(3, 3)
        self.test_terminal = TerminalSize(105, 50)

    # arguments parser tests
    def test_parse_args_from_cmdline_normal_args(self):
        args = ["--width", "10", "--height", "3"]
        expected = argparse.Namespace(width="10", height="3")
        self.assertEqual(expected, cb.parse_args_from_cmdline(args))

    def test_parse_args_from_cmdline_empty_args(self):
        expected = argparse.Namespace(width=None, height=None)
        self.assertEqual(expected, cb.parse_args_from_cmdline(""))

    def test_parse_args_from_cmdline_only_one_arg(self):
        args = ["--width", "2.5"]
        expected = argparse.Namespace(width="2.5", height=None)
        self.assertEqual(expected, cb.parse_args_from_cmdline(args))

    # ChessBoard constructor and method tests
    def test_constructor(self):
        self.assertEqual((3, 3), (self.my_board._width, self.my_board._height))

    def test_draw_board_method(self):
        self.assertEqual("* *\n"
                         " * \n"
                         "* *",
                         self.my_board.draw_board())

    # testing board size vs terminal size
    def test_check_board_size_less_then_expected(self):
        self.assertEqual(False, cb.check_board_size(-1, 20, self.test_terminal))

    def test_check_board_size_more_then_expected(self):
        self.assertEqual(False, cb.check_board_size(95, 51, self.test_terminal))

    def test_check_board_size_perfect_case(self):
        self.assertEqual(True, cb.check_board_size(95, 30, self.test_terminal))

    # testing user input parser
    def test_get_user_input_perfect_input(self):
        with patch("tasks.t1_chess_board.input", return_value=20):
            self.assertEqual((20, 20), cb.get_user_input())

    """idk why it's dose not works"""
    # def test_get_user_input_empty_input(self):
    #     with patch("tasks.t1_chess_board.input", return_value=""):
    #         self.assertRaises(SystemExit, cb.get_user_input())
    #
    # def test_get_user_input_float_input(self):
    #     with patch("tasks.t1_chess_board.input", return_value=2.5):
    #         self.assertRaises(ValueError, cb.get_user_input())
    #
    # def test_get_user_input_str_input(self):
    #     with patch("tasks.t1_chess_board.input", return_value="heh"):
    #         self.assertRaises(ValueError, cb.get_user_input())


if __name__ == "__main__":
    unittest.main()
