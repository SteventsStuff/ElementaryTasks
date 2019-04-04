#!/usr/bin/env python3
import sys
from pathlib import Path
import argparse


def main():
    args = parse_args_from_cmdline(sys.argv[1:])

    print("Generating tickets...")
    tickets_list = generate_lucky_tickets()

    method = ""
    if Path(args.file_path).is_file():
        method = get_file_content(args.file_path)

    if method:
        print("Counting...")
        res_data = count_tickets(method, tickets_list)
    else:
        method = get_user_input_method()
        res_data = count_tickets(method, tickets_list)

    if res_data:
        print(f"You got {res_data[0]} lucky tickets, using '{res_data[1]}' method!")
    else:
        print("There is no lucky tickets...")


def generate_lucky_tickets():
    return [f"{num:06}" for num in range(1000000)]


def get_file_content(file_name) -> str:
    file = open(file_name, "r")
    method = file.readline().strip().lower()
    file.close()

    if method:
        if method in ("moscow", "piter"):
            print(f"'{method}' will be used!")
            return method
        else:
            print(f"'{method[:-1]}' is invalid!")
            return ""
    else:
        print("Your file is empty!")
        return ""


def count_tickets(method, tickets_list) -> (int, str):
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

    return counter, method


def get_user_input_method() -> str:
    print("Interactive mode:")
    user_method = ""
    print("Enter empty line to exit")
    while user_method.lower() not in ("moscow", "piter"):
        user_method = input("Enter method ('moscow' or 'piter'): ")
        if user_method == "":
            exit()

    print("Counting...")
    return user_method


def parse_args_from_cmdline(argv):
    parser = argparse.ArgumentParser(
        prog="Lucky_tickets",
        description="Count amount of lucky tickets depends on count method")
    parser.add_argument("--file", dest="file_path", default="",
                        help="set file path with method name")
    return parser.parse_args(argv)


if __name__ == "__main__":
    main()
