#!/usr/bin/env python3

import sys
from pathlib import Path
from tasks_args_parser import *


def main():
    args = parse_args_from_cmdline_6(sys.argv[1:])

    print("Generating tickets...")
    tickets_list = [f"{num:06}" for num in range(1000000)]

    if Path(args.file_name).is_file():
        method = get_file_content(args.file_name)
        if method:
            count_tickets(method, tickets_list)
        else:
            activate_interactive_mode(tickets_list)
    else:
        activate_interactive_mode(tickets_list)


def get_file_content(file_name):
    file = open(file_name, "r")
    method = file.readline().strip().lower()
    file.close()

    if method:
        if method in ("moscow", "piter"):
            print(f"'{method}' will be used!")
            return method
        else:
            print(f"'{method}' is invalid!")
    else:
        print("Your file is empty!")


def count_tickets(method, tickets_list):
    print("Counting...")
    counter = 0
    for ticket in tickets_list:
        if method == "moscow":
            left_side = sum([int(digit) for digit in ticket[:3]])
            right_side = sum([int(digit) for digit in ticket[3:]])
            if left_side == right_side:
                counter += 1

        if method == "piter":
            odd = sum([int(digit) for digit in ticket[::2]])
            even = sum([int(digit) for digit in ticket[1::2]])
            if odd == even:
                counter += 1

    print(f"You got {counter} lucky tickets, using {method} method!")


def activate_interactive_mode(tickets_list):
    print("Interactive mode:")
    user_method = ""
    while user_method.lower() not in ("moscow", "piter"):
        user_method = input("Enter method ('moscow' or 'piter'): ")

    count_tickets(user_method.lower(), tickets_list)


if __name__ == "__main__":
    main()
