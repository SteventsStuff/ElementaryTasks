"""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 2
"""

from tasks_opt_parsesr import *


def envelope_comparing(envelope_sides):
    """
    comparing two Envelope objects
    :return True if envelope1 can be put in envelope2
    """
    print("\nEnvelop number one: ", end="")
    my_envelope_one = Envelope(envelope_sides[0], envelope_sides[1])
    print("The first envelope has been successfully created!")
    print("Envelop number two: ", end="")
    my_envelope_two = Envelope(envelope_sides[2], envelope_sides[3])
    print("The second envelope was successfully created!\n")

    if my_envelope_two < my_envelope_one:
        print("You can put one envelope in another")
    elif my_envelope_one < my_envelope_two:
        print("You can put one envelope in another")
    else:
        print("You can NOT put one envelope in another")


class Envelope:
    def __init__(self, side_a, side_b):
        self.IM_flag = False
        while True:
            try:
                if self.IM_flag:
                    self.__side_a = float(input("Enter first side: "))
                    self.__side_b = float(input("Enter second side: "))
                else:
                    self.__side_a = float(side_a)
                    self.__side_b = float(side_b)

                if not (self.__side_a > 0 and self.__side_b > 0):
                    raise ValueError
                else:
                    break
            except (TypeError, ValueError):
                print()
                self.IM_flag = True

    def __lt__(self, other):
        if self.__side_a < other.__side_a and self.__side_b < other.__side_b:
            return True
        else:
            return False


if __name__ == "__main__":
    sides = set_opts_task2()

    while True:
        envelope_comparing(sides)

        sides = [0, 0, 0, 0]
        user_choose = input("Do you want to try one more time? [Y/N]: ")
        if user_choose.lower() == 'y' or user_choose.lower() == 'yes':
            continue
        else:
            break
