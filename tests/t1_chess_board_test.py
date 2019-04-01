#!/usr/bin/env python3
import unittest
import argparse
import tasks.t1_chess_board as cb
from tasks.t1_chess_board import ChessBoard


class TestChessBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.my_board = ChessBoard(3, 3)

    # ChessBoard constructor and method tests
    def test_constructor(self):
        self.assertEqual((3, 3), (self.my_board._width, self.my_board._height))

    def test_draw_board_method(self):
        self.assertEqual("* *\n"
                         " * \n"
                         "* *",
                         self.my_board.draw_board())

    # arguments parser tests
    def test_parse_args_from_cmdline(self):
        args = ["--width", "10", "--height", "3"]
        expected = argparse.Namespace(width="10", height="3")
        self.assertEqual(expected, cb.parse_args_from_cmdline(args))


if __name__ == "__main__":
    unittest.main()
