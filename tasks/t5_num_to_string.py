#!/usr/bin/env python3

import sys
import argparse


def num2words(num):
    nums_0_19 = ['Zero', 'One', 'Two', 'Three', 'Four',
                 'Five', 'Six', 'Seven', 'Eight', "Nine",
                 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    nums_20_90 = ['Twenty', 'Thirty', 'Forty', 'Fifty',
                  'Sixty', 'Seventy', 'Eighty', 'Ninety']

    nums_dict = {100: 'Hundred',
                 1000: 'Thousand',
                 1000000: 'Million',
                 1000000000: 'Billion'}

    if num < 0:
        return "Minus " + num2words(abs(num))
    if num < 20:
        return nums_0_19[num]
    if num < 100:
        res = nums_20_90[num//10 - 2]
        if num % 10 == 0:
            res += ""
        else:
            res += " " + nums_0_19[num % 10]
        return res

    max_key = max([key for key in nums_dict.keys() if key <= num])
    res = num2words(num//max_key) + " " + nums_dict[max_key]
    if num % max_key == 0:
        res += ""
    else:
        res += " " + num2words(num % max_key)
    return res


def main():
    args = parse_args_from_cmdline(sys.argv[1:])

    if args.num:
        try:
            args.num = int(args.num)
            print(num2words(args.num))
            exit()
        except ValueError:
            print("Invalid input!\nInteractive mode:")

    print("Interactive mode:")
    number = get_user_input()
    print(num2words(number))


def get_user_input():
    while True:
        try:
            print("Enter empty line to exit")
            num = input("Enter number: ")
            if num == "":
                exit()
            num = int(num)
            return num
        except ValueError:
            print("Invalid input!")


def parse_args_from_cmdline(argv):
    parser = argparse.ArgumentParser(
        prog="Num_to_str",
        description="Convert number to a string")
    parser.add_argument("--num", dest="number",
                        default="0", help="set number to convert")
    return parser.parse_args(argv)


if __name__ == "__main__":
    main()
