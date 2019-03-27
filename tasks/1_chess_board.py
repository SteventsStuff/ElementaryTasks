#!/usr/bin/env python3
import sys
import os
import argparse


def main():
    args = parse_args_from_cmdline(sys.argv[1:])
    terminal_size = os.get_terminal_size()
    if args.author:
        print("""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 1
""")

    if not (args.width and args.height):
        print("Interactive mode:")
        activate_interactive_mode(terminal_size)
    else:
        if check_user_input(args.width, args.height, terminal_size):
            print(ChessBoard(args.height, args.width).draw_board())


def activate_interactive_mode(terminal_size):
    width, height = get_chess_board_size()
    if check_user_input(width, height, terminal_size):
        print(ChessBoard(width, height).draw_board())


def get_chess_board_size():
    while True:
        try:
            user_width = int(input("Enter chess board WIDTH: "))
            user_height = int(input("Enter chess board HEIGHT: "))
            return user_width, user_height
        except ValueError:
            print("WIDTH/HEIGHT must be integers!\n")


def check_user_input(w, h, term_size):
    if (w >= term_size.columns or h >= term_size.lines) or (w < 1 or h < 1):
        print("\nInvalid size!")
        print(f"WIDTH must be between 1 and {term_size.columns + 1}")
        print(f"HEIGHT must be between 1 and {term_size.lines + 1}\n")
        activate_interactive_mode(term_size)
    else:
        return True


def parse_args_from_cmdline(argv):
    parser = argparse.ArgumentParser(
        prog="Chess_board",
        description="This program creates chess board with A*B size",
    )
    parser.add_argument("--author", action="store_true",
                        default=False, help="print author information")
    parser.add_argument("--width", type=int, help="set chess board width")
    parser.add_argument("--height", type=int, help="set chess board height")
    args = parser.parse_args(argv)
    return args


class ChessBoard:
    def __init__(self, height, width):
        """Create chess board with size width * height"""
        self._width = width
        self._height = height

    def draw_board(self):
        """Draw chess board"""
        board_str = ""
        for h in range(1, self._width + 1):
            for elem in range(h,  self._height + h):
                if elem % 2 == 0:
                    board_str += " "
                else:
                    board_str += "*"
            board_str += "\n"

        return board_str[:-1]


if __name__ == "__main__":
    main()
