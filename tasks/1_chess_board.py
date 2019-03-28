#!/usr/bin/env python3
import sys
import os
from tasks_args_parser import *


def main():
    args = parse_args_from_cmdline_1(sys.argv[1:])
    terminal_size = os.get_terminal_size()

    if args.width and args.height:
        try:
            args.width = int(args.width)
            args.height = int(args.height)
            if check_board_size(args.width, args.height, terminal_size):
                print(ChessBoard(args.width, args.height).draw_board())
        except ValueError:
            print("Invalid values!")
            print("Interactive mode:")
            activate_interactive_mode(terminal_size)
    else:
        print("Interactive mode:")
        activate_interactive_mode(terminal_size)


def activate_interactive_mode(terminal_size):
    user_width, user_height = get_user_input()
    if check_board_size(user_width, user_height, terminal_size):
        print(ChessBoard(user_width, user_height).draw_board())


def get_user_input():
    while True:
        try:
            user_width = int(input("Enter chess board WIDTH: "))
            user_height = int(input("Enter chess board HEIGHT: "))
            return user_width, user_height
        except ValueError:
            print("WIDTH/HEIGHT must be integers!\n")


def check_board_size(width, height, term_size):
    if not (0 < width < term_size.columns and 0 < height < term_size.lines):
        print("\nInvalid size!")
        print(f"WIDTH must be min: 1 and max: {term_size.columns - 1}")
        print(f"HEIGHT must be min: 1 and max: {term_size.lines - 1}\n")
        activate_interactive_mode(term_size)
    else:
        return True


class ChessBoard:
    def __init__(self, width, height):
        """Create chess board with size width * height"""
        self._width = width
        self._height = height

    def draw_board(self):
        """Draw chess board"""
        board_str = ""
        for h in range(1, self._height + 1):
            for elem in range(h,  self._width + h):
                if elem % 2 == 0:
                    board_str += " "
                else:
                    board_str += "*"
            board_str += "\n"

        return board_str[:-1]


if __name__ == "__main__":
    main()
