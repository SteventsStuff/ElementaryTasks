"""Module for parsing options and arguments for elementary tasks."""

import optparse
import random


def create_general_parser(usage="%prog [options]"):
    """Create options for help information (version, author)"""
    version = "%prog 0.1 (No Unit Tests)"
    general_parser = optparse.OptionParser(version=version, usage=usage)
    general_parser.add_option("-a", "--author",
                              help="get information about author",
                              action="store_true", default=False,
                              dest="author")
    return general_parser


def print_author(options, task_num):
    if options.author:
        print("Author information:")
        print("Group:\t\tDP158Py\nStudent:\tMiroshnychenko V.")
        print(f"Task:\t\tTask{task_num}")
        exit()


def set_opts_task1():
    """Add task 1 options.
    :return: tuple (width, height)
    """
    usage = """usage: %prog [options]
       %prog [no-options: interactive mode]"""
    task_parser = create_general_parser(usage)

    task_parser.add_option("-W", "--width",
                           default="0.1", dest="width",
                           help="set board width")
    task_parser.add_option("-H", "--height",
                           default="0.1", dest="height",
                           help="set board height")
    options = task_parser.parse_args()[0]
    print_author(options, 1)
    return options.width, options.height


def set_opts_task2():
    """Add task 2 options.
    :return: tuple (sideA, sideB, sideC, sideD)
    """
    usage = """usage: %prog [options]
       %prog [no-options: interactive mode]"""
    task_parser = create_general_parser(usage)

    task_parser.add_option("-A", dest="sideA", help="set a side")
    task_parser.add_option("-B", dest="sideB", help="set b side")
    task_parser.add_option("-C", dest="sideC", help="set c side")
    task_parser.add_option("-D", dest="sideD", help="set d side")

    options = task_parser.parse_args()[0]
    print_author(options, 2)

    return options.sideA, options.sideB, options.sideC, options.sideD


def set_opts_task3():
    """Has no other options."""
    usage = """%prog [no-options: interactive mode]"""
    task_parser = create_general_parser(usage)

    options = task_parser.parse_args()[0]
    print_author(options, 3)


def set_opts_task4():
    """Has no other options.
    :return: tuple of args (file_name find_str [optional: replace_str])
    """
    usage = """usage: %prog [args: <file_name> <find_str> <replace_str>]"""
    task_parser = create_general_parser(usage)

    options, args = task_parser.parse_args()
    print_author(options, 4)
    return args


def set_args_task6():
    """Add task 6 options.
    :return: file_name
    """
    usage = """usage: %prog [options]"""
    task_parser = create_general_parser(usage)
    task_parser.add_option("-f", "--file",
                           help="file with tickets [default: tickets.txt]",
                           default="tickets.txt",
                           dest="file_name")
    task_parser.add_option("-m", "--method",
                           help="set method easy | hard [default: easy]",
                           dest="method",
                           default="easy")

    options = task_parser.parse_args()[0]
    print_author(options, 5)
    generate_tickets(options.file_name, options.method)

    return options.file_name


def generate_tickets(file_name, method, amount=500):
    """generate N tickets with easy | hard methods"""
    f = open(file_name, "w")
    if method == "easy":
        f.writelines("easy\n")
    elif method == "hard":
        f.writelines("hard\n")
    else:
        f.writelines("easy hard\n")

    for i in range(amount):
        val = str(random.randint(100000, 999999))
        f.writelines(f'{val}\n')
    f.close()
