"""Module for parsing options ang arguments for elementary tasks.

Has function for create general options for every task and
set of functions for every task.

!!!FOR NOW: IF OPTION HAS NOT PARAMETER PROGRAM STOPS!!!

Funcs:
     create_general_parser(usage: str)
     set_opts_task1(): options: (-W --width, -H --height)
     set_opts_task2(): options: (-A -B -C -D)
     set_opts_task3()
     set_opts_task4()
     set_opts_task5()
     set_opts_task6()
     set_opts_task7()
     set_opts_task8()
     set_opts_task9()
"""

import optparse


def create_general_parser(usage="%prog [options]"):
    """
    Create options for help information about:
    - version
    - author
    """
    version = "%prog 0.1 (No Unit Tests)"
    general_parser = optparse.OptionParser(version=version,
                                           usage=usage)
    general_parser.add_option("-a", "--author",
                              help="get information about author",
                              action="store_true",
                              default=False,
                              dest="author")

    return general_parser


def print_author(options, task_num):
    if options.author:
        print("Author information:")
        print("Group:\t\tDP158Py\nStudent:\tMiroshnychenko V.")
        print(f"Task:\t\tTask{task_num}")
        exit()


def set_opts_task1():
    """
    Add task 1 options:
    - set width (-W --width)
    - set height (-H --height)

    :return: tuple of options.width,
                      options.height
    """
    usage = """usage: %prog [options]
       %prog [no-options: interactive mode]"""
    task_parser = create_general_parser(usage)
    task_parser.add_option("-W", "--width",
                           dest="width",
                           help="set board width")
    task_parser.add_option("-H", "--height",
                           dest="height",
                           help="set board height")

    options = task_parser.parse_args()[0]
    print_author(options, 1)

    return options.width, options.height


def set_opts_task2():
    """
    Add task 2 options:
    - set side A size (-A)
    - set side B size (-B)
    - set side C size (-C)
    - set side D size (-D)

    :return: tuple of options.width,
                      options.height
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
