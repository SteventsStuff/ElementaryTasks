#!/usr/bin/env python3

import sys
from tasks_args_parser import *


def main():
    args = parse_args_from_cmdline_8(sys.argv[1:])
    print(args)

    if args[0] and args[1]:
        try:
            int_min = int(args[0])
            int_max = int(args[1])
            if not 0 <= int_min < int_max:
                raise ValueError
            print_fibo(int_min, int_max)
        except (TypeError, ValueError):
            print(print_invalid_args_message())
            activate_interactive_mode()
    else:
        activate_interactive_mode()


def print_invalid_args_message():
    return "Invalid arguments!"


def activate_interactive_mode():
    print("Interactive mode:")
    while True:
        try:
            print("Enter empty lines to exit")
            min_val = input("Enter min value: ")
            max_val = input("Enter max value: ")
            if min_val == "" and max_val == "":
                exit()
            min_val, max_val = int(min_val), int(max_val)
            if not 0 <= min_val < max_val:
                raise ValueError
            print_fibo(min_val, max_val)
            break
        except (TypeError, ValueError):
            print(print_invalid_args_message())


def fibonacci_seq():
    num1, num2 = 0, 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


def print_fibo(start, end):
    generator = fibonacci_seq()
    while True:
        number = next(generator)
        if start <= number < end:
            print(number, end=" ")
        elif number >= end:
            print()
            break


if __name__ == "__main__":
    main()
