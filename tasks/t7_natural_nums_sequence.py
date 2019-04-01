#!/usr/bin/env python3
import sys
import argparse


def main():
    args = parse_args_from_cmdline_7(sys.argv[1:])

    if args.number:
        try:
            num = int(args.number)
            if num < 1:
                raise ValueError
            print([x for x in range(num) if x**2 < num and x > 0])
        except (TypeError, ValueError):
            activate_interactive_mode()
    else:
        activate_interactive_mode()


def print_invalid_input_message():
    return "Invalid input!"


def activate_interactive_mode():
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
        except (TypeError, ValueError):
            print(print_invalid_input_message())
        else:
            print([x for x in range(number) if x ** 2 < number and x > 0])
            break


def parse_args_from_cmdline_7(argv):
    parser = argparse.ArgumentParser(
        prog="Natural_nums_sequence",
        description="""Displays sequence of numbers, power of which less
         than entered number""")
    parser.add_argument("--number", help="set border number")
    return parser.parse_args(argv)


if __name__ == "__main__":
    main()
