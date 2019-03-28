import argparse


def parse_args_from_cmdline_1(argv):
    parser = argparse.ArgumentParser(
        prog="Chess_board",
        description="This program creates chess board with WIDTH*HEIGHT size")
    parser.add_argument("--width", help="set chess board width (int)")
    parser.add_argument("--height", help="set chess board height (int)")
    return parser.parse_args(argv)


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


def parse_args_from_cmdline_5(argv):
    parser = argparse.ArgumentParser(
        prog="Num_to_str",
        description="Convert number to a string")
    parser.add_argument("--num", dest="number",
                        default="0", help="set number to convert")
    return parser.parse_args(argv)


def parse_args_from_cmdline_6(argv):
    parser = argparse.ArgumentParser(
        prog="Lucky_tickets",
        description="Count amount of lucky tickets depends on count method")
    parser.add_argument("--file", dest="file_name", default="",
                        help="set file with method name")
    return parser.parse_args(argv)


def parse_args_from_cmdline_7(argv):
    parser = argparse.ArgumentParser(
        prog="Natural_nums_sequence",
        description="""Displays sequence of numbers, power of which less
         than entered number""")
    parser.add_argument("--number", help="set border number")
    return parser.parse_args(argv)


def parse_args_from_cmdline_8(argv):
    parser = argparse.ArgumentParser(
        prog="Fibonacci_numbers",
        description="Displays sequence of fibonacci numbers, in range")
    parser.add_argument("--min", help="set min possible number")
    parser.add_argument("--max", help="set max possible number")
    args = parser.parse_args(argv)
    return args.min, args.max

