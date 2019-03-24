"""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 4
"""

from tasks_opt_parsesr import *
import pathlib


def parse_file(file_name, arguments, mode):
    file_r = open(file_name, "r")

    if mode == 2:
        text_tmp = "".join(file_r.read().split("\n"))
        counter = text_tmp.count(arguments[1])
        print(f'"{arguments[1]}" meets {counter} times')

    else:
        tmp_list = file_r.read().split(arguments[1])
        new_text = arguments[2].join(tmp_list)

        file_w = open(file_name, "w")
        file_w.write(new_text)
        file_w.close()

    file_r.close()


if __name__ == "__main__":
    args = set_args_task4()
    print(args)

    if len(args) >= 2 and pathlib.Path(args[0]).is_file():
        parse_file(args[0], args, len(args))
    else:
        print("Interactive mode:")
        while True:
            file = input("Enter file name: ")
            if pathlib.Path(file).is_file():
                parse_file(file, args, len(args))
            else:
                print("File not found!")
                continue
