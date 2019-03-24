"""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 6
"""

from tasks_opt_parsesr import *


def use_easy_method(number):
    left_part = 0
    right_part = 0
    for char in number[0:3]:
        left_part += int(char)
    for char in number[3:]:
        right_part += int(char)

    if left_part == right_part:
        print(f"{number} is lucky [using easy method]")


def use_hard_method(number):
    even = 0
    odd = 0
    for i in range(1, 7):
        if i % 2 == 0:
            even += int(number[i - 1])
        else:
            odd += int(number[i - 1])

    if even == odd:
        print(f"{number} is lucky [using hard method]")


if __name__ == "__main__":
    file_name = set_args_task6()

    file = open(file_name, "r")
    method = file.readline()
    numbers = file.read().split("\n")

    for num in numbers:
        if method == "easy":
            use_easy_method(num)
        elif method == "hard":
            use_hard_method(num)

    file.close()
