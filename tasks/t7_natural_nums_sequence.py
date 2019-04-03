#!/usr/bin/env python3
import sys
import argparse


def main():
    args = parse_args_from_cmdline(sys.argv[1:])

    if args.number:
        try:
            num = int(args.number)
            if num < 1:
                raise ValueError
            print(get_sequence(num))
            exit()
        except (TypeError, ValueError):
            print("Invalid input!")

    num = get_user_input()
    print(get_sequence(num))


def get_sequence(number):
    return [x for x in range(number) if x ** 2 < number and x > 0]


def get_user_input():
    print("You need to enter positive integer number!")
    while True:
        try:
            print("Enter empty line to exit")
            number = int(input("Enter number: "))
            if number == "":
                exit()
            number = int(number)
            if number < 1:
                raise ValueError
            return number
        except (TypeError, ValueError):
            print("Invalid input!")


def parse_args_from_cmdline(argv):
    parser = argparse.ArgumentParser(
        prog="Natural_nums_sequence",
        description="""Displays sequence of numbers, power of which less
         than entered number""")
    parser.add_argument("--number", help="set border number")
    return parser.parse_args(argv)


if __name__ == "__main__":
    main()
