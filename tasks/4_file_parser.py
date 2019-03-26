"""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 4
"""

import pathlib
import sys


def parse_file(is_find_mode, file_name, str_find, str_replace=None):
    """Depends on mode, search how many times <str_find> meets in file,
     or search <str_find> and replace it with <str_replace>
    """
    file_r = open(file_name, "r")

    if is_find_mode:
        text_tmp = "".join(file_r.read().split("\n"))
        counter = text_tmp.count(str_find)
        print(f'"{str_find}" meets {counter} times')

    else:
        tmp_list = file_r.read().split(str_find)
        new_text = str_replace.join(tmp_list)

        file_w = open(file_name, "w")
        file_w.write(new_text)
        file_w.close()

    file_r.close()


if __name__ == "__main__":
    args = sys.argv

    if len(args) >= 3 and pathlib.Path(args[1]).is_file():
        if len(args) == 3:
            parse_file(True, args[1], args[2])
        else:
            parse_file(False, args[1], args[2], args[3])
    else:
        print("Interactive mode:")
        while True:
            file = input("Enter file name: ")
            find_str = input("Enter str to find: ")
            replace_str = input("Enter str to replace [optional]: ")

            if pathlib.Path(file).is_file() and find_str and not replace_str:
                parse_file(True, file, find_str)
                break
            elif pathlib.Path(file).is_file() and find_str and replace_str:
                parse_file(False, file, find_str, replace_str)
                break
            else:
                print("Invalid input\n")
                continue
