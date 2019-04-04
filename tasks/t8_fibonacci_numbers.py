#!/usr/bin/env python3
import sys
import argparse


def main():
    args = parse_args_from_cmdline(sys.argv[1:])

    if args[0] and args[1]:
        try:
            int_min = int(args[0])
            int_max = int(args[1])
            if not 0 <= int_min < int_max:
                raise ValueError
            print_fibo(int_min, int_max)
            exit()
        except (TypeError, ValueError):
            print("Invalid arguments!")

    print("Interactive mode:")
    usr_min, usr_max = get_user_input()
    print_fibo(usr_min, usr_max)


def get_user_input():
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
            return min_val, max_val
        except ValueError:
            print("Invalid arguments!")


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


def parse_args_from_cmdline(argv):
    parser = argparse.ArgumentParser(
        prog="Fibonacci_numbers",
        description="Displays sequence of fibonacci numbers, in range")
    parser.add_argument("--min", help="set min possible number")
    parser.add_argument("--max", help="set max possible number")
    args = parser.parse_args(argv)
    return args.min, args.max


if __name__ == "__main__":
    main()
