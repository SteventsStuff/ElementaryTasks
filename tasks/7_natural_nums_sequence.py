#!/usr/bin/env python3

import sys
from tasks_args_parser import *


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


def activate_interactive_mode():
    print("You need to enter positive integer number!")
    while True:
        try:
            number = int(input("Enter number: "))
            if number < 1:
                raise ValueError
        except (TypeError, ValueError):
            print("Invalid value!")
        else:
            print([x for x in range(number) if x ** 2 < number and x > 0])
            break


if __name__ == "__main__":
    main()
