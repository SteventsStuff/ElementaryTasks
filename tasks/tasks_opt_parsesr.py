"""Module for parsing options and arguments for elementary tasks."""

import optparse
import random


def create_general_parser(usage="%prog [options]"):
    """Create options for help information (version, author)"""
    version = "%prog 0.1 (No Unit Tests)"
    general_parser = optparse.OptionParser(version=version, usage=usage)
    general_parser.add_option("-a", "--author", help="get information about author",
                              action="store_true", default=False, dest="author")
    return general_parser


def print_author(task_num):
    print("Author information:\nGroup:\t\tDP158Py\nStudent:\tMiroshnychenko V.")
    print(f"Task:\t\tTask{task_num}")
    exit()


def get_task1_options():
    """Add task 1 options. :return: tuple (width, height)"""
    usage = """usage: %prog [options]
       %prog [no-options: interactive mode]"""
    task_parser = create_general_parser(usage)
    task_parser.add_option("-W", "--width", dest="width", help="set board width")
    task_parser.add_option("-H", "--height", dest="height", help="set board height")

    return task_parser.parse_args()[0]


def parse_task1_options():
    options = get_task1_options()
    interactive_mode = False

    if options.author:
        print_author(1)

    while True:
        try:
            if interactive_mode:
                width = int(input("Enter chess board width: "))
                height = int(input("Enter chess board height: "))
            else:
                width = int(options.width)
                height = int(options.height)

            if width < 0 or height < 0:
                raise ValueError
        except (TypeError, ValueError):
            interactive_mode = True
            continue
        else:
            break

    return width, height


def set_args_task6():
    """Add task 6 options.
    :return: file_name
    """
    usage = """usage: %prog [options]"""
    task_parser = create_general_parser(usage)
    task_parser.add_option("-f", "--file", help="file with tickets [default: tickets.txt]",
                           default="tickets.txt", dest="file_name")
    task_parser.add_option("-m", "--method", help="set method easy | hard | mixed [default: easy]",
                           dest="method", default="easy")
    task_parser.add_option("-n", "--number", help="set method amount of tickets [default: 500]",
                           dest="tickets", default="500")

    options = task_parser.parse_args()[0]
    print_author(options, 6)
    try:
        tickets_num = int(options.tickets)
        if tickets_num < 0:
            raise ValueError
    except (TypeError, ValueError):
        print(f"Invalid input. '{options.file_name}' will has 500 tickets")
        generate_tickets(options.file_name, options.method)
    else:
        generate_tickets(options.file_name, options.method, tickets_num)

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
        val = "{:06}".format(random.randint(0, 999999))
        f.writelines(f'{val}\n')
    f.close()
