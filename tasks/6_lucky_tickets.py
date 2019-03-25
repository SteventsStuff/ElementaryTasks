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

    return left_part == right_part


def use_hard_method(number):
    even = 0
    odd = 0
    for i in range(1, 7):
        if i % 2 == 0:
            even += int(number[i - 1])
        else:
            odd += int(number[i - 1])

    return even == odd


if __name__ == "__main__":
    file_name = set_args_task6()
    file = open(file_name, "r")

    method_list = file.readline().split()
    numbers = file.read().split("\n")[:-1]
    counter_easy = 0
    counter_hard = 0

    for num in numbers:
        if "easy" in method_list:
            if use_easy_method(num):
                counter_easy += 1
                print(f"{num} is lucky [using easy method]")
        if "hard" in method_list:
            if use_hard_method(num):
                counter_hard += 1
                print(f"{num} is lucky [using hard method]")

    print()
    if counter_easy:
        print(f"{counter_easy} lucky tickets using easy method ")
    if counter_hard:
        print(f"{counter_hard} lucky tickets using hard method ")

    file.close()
