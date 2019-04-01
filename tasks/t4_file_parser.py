#!/usr/bin/env python3
import pathlib
import sys
import argparse


def main():
    file_name, find_str, replace_str = parse_args_from_cmdline_4(sys.argv[1:])

    if pathlib.Path(file_name).is_file() and find_str:
        if replace_str:
            parse_file(file_name, find_str, replace_str)
        else:
            parse_file(file_name, find_str)
    else:
        print("Interactive mode:")
        activate_interactive_mode()


def print_no_file_found_message():
    return "No file with this name!\n"


def activate_interactive_mode():
    while True:
        try:
            print("Enter empty lines to exit")
            file_name = input("Enter file name: ")
            find_str = input("Enter string for search: ")
            replace_str = input("Enter string to replace (optional): ")
            if not (file_name, find_str, replace_str):
                exit()
            if not pathlib.Path(file_name).is_file():
                raise FileNotFoundError
            if replace_str and find_str:
                parse_file(file_name, find_str, replace_str)
            elif find_str:
                parse_file(file_name, find_str)
            else:
                print("You need at least to enter string for search!\n")
            break
        except FileNotFoundError:
            print(print_no_file_found_message())


def parse_file(file_name, str_find, str_replace=None):
    """Depends on mode, search how many times <str_find> meets in file,
     or search <str_find> and replace it with <str_replace>
    """
    file = open(file_name, "r")

    if str_replace:
        tmp_list = file.read().split(str_find)
        new_text = str_replace.join(tmp_list)

        file_w = open(file_name, "w")
        file_w.write(new_text)
        file_w.close()
        print("File was changed!")
    else:
        text_tmp = "".join(file.read().split("\n"))
        counter = text_tmp.count(str_find)
        print(f'"{str_find}" meets {counter} times')

    file.close()


def parse_args_from_cmdline_4(argv):
    parser = argparse.ArgumentParser(
        prog="File_parser",
        description="""Count entries of <string> you need to 
                    enter 2 params: --file --find_str
                    Replace <str1> with <str2> enter 3 params:
                    --file --find_str --replace_str""")
    parser.add_argument("--file", dest="file_path",
                        default="", help="set file with test name")
    parser.add_argument("--find", dest="find_str",
                        help="set a string which needs to be found")
    parser.add_argument("--replace", dest="replace_str",
                        help="set a string to replace")
    args = parser.parse_args(argv)
    return args.file_path, args.find_str, args.replace_str


if __name__ == "__main__":
    main()