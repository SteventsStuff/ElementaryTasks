#!/usr/bin/env python3
import sys
import os
import argparse


def main():
    args = parse_args_from_cmdline(sys.argv[1:])
    terminal_size = os.get_terminal_size()

    if args.width and args.height:
        try:
            args.width = int(args.width)
            args.height = int(args.height)
            if check_board_size(args.width, args.height, terminal_size):
                print(ChessBoard(args.width, args.height).draw_board())
                exit()
        except ValueError:
            print("Invalid values!")

    print("Interactive mode:")
    while True:
        user_width, user_height = get_user_input()
        if check_board_size(user_width, user_height, terminal_size):
            print(ChessBoard(user_width, user_height).draw_board())
            break


def get_user_input() -> (int, int):
    while True:
        try:
            print("Enter empty lines to exit")
            user_width = input("Enter chess board WIDTH: ")
            user_height = input("Enter chess board HEIGHT: ")
            if user_height == "" and user_width == "":
                exit()
            user_width, user_height = int(user_width), int(user_height)
            return user_width, user_height
        except ValueError:
            print("WIDTH/HEIGHT must be integers!\n")


def check_board_size(width, height, term_size) -> bool:
    if not (0 < width < term_size.columns and 0 < height < term_size.lines):
        print("\nInvalid size!")
        print(f"WIDTH must be min: 1 and max: {term_size.columns - 1}")
        print(f"HEIGHT must be min: 1 and max: {term_size.lines - 1}\n")
        return False
    else:
        return True


def parse_args_from_cmdline(argv):
    parser = argparse.ArgumentParser(
        prog="Chess_board",
        description="This program creates chess board with WIDTH*HEIGHT size")
    parser.add_argument("--width", help="set chess board width (int)")
    parser.add_argument("--height", help="set chess board height (int)")
    return parser.parse_args(argv)


class ChessBoard:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def draw_board(self):
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
