"""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 8
"""

import sys


def interactive_mode():
    print("Interactive mode:")
    while True:
        try:
            min_val = int(input("Enter min value: "))
            max_val = int(input("Enter max value: "))
            if not 0 <= min_val < max_val:
                raise ValueError
        except (TypeError, ValueError):
            print("Invalid arguments!")
            continue
        else:
            print_fibo(min_val, max_val)
            break


def fibonacci_seq():
    num1, num2 = 0, 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


def print_fibo(start, end):
    print("Loading...")
    generator = fibonacci_seq()
    while True:
        number = next(generator)
        if start <= number < end:
            print(number, end=", ")
        elif number >= end:
            print()
            break


if __name__ == "__main__":
    args = sys.argv

    if len(args) >= 3:
        try:
            int_min = int(args[1])
            int_max = int(args[2])
            if not 0 <= int_min < int_max:
                raise ValueError
        except (TypeError, ValueError):
            print("Invalid arguments!")
            interactive_mode()
        else:
            print_fibo(int_min, int_max)
    else:
        interactive_mode()
