"""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 7
"""

import sys


def interactive_mode():
    while True:
        try:
            number = int(input("Enter number: "))
            if not number > 0:
                raise ValueError
        except (TypeError, ValueError):
            print("Invalid size!")
            continue
        else:
            print([x for x in range(number) if x ** 2 < number])
            break


if __name__ == "__main__":
    args = sys.argv

    if len(args) > 1:
        try:
            num = int(args[1])
            if not num > 0:
                raise ValueError
            print([x for x in range(num) if x**2 < num])
        except (TypeError, ValueError):
            interactive_mode()
    else:
        print("You need to enter positive integer number!")
        interactive_mode()
