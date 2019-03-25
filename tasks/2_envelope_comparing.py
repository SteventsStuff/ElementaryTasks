"""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 2
"""


class Envelope:
    def __init__(self, side_a, side_b):
        """This class creates envelope with size: A*B
        and provides possibility for comparing two envelope.
        """
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

            except (TypeError, ValueError):
                print("(You need to enter positive float values)")
                self.IM_flag = True
            else:
                break

    def __lt__(self, other):
        """Method for comparing two objects.
        :return: True if self object is bigger or False otherwise
        """
        if self.__side_a < other.__side_a and self.__side_b < other.__side_b:
            return True
        else:
            return False


if __name__ == "__main__":
    print("This program checks if it's possible to put one envelope another")

    while True:
        print("\nEnvelop number one: ")
        my_envelope_one = Envelope(side_a=input("Enter first side: "),
                                   side_b=input("Enter second side: "))
        print("The first envelope has been successfully created!")

        print("\nEnvelop number two: ")
        my_envelope_two = Envelope(side_a=input("Enter first side: "),
                                   side_b=input("Enter second side: "))
        print("The second envelope has been successfully created!\n")

        if my_envelope_two < my_envelope_one:
            print("You can put one envelope in another")
        elif my_envelope_one < my_envelope_two:
            print("You can put one envelope in another")
        else:
            print("You can NOT put one envelope in another")

        user_choose = input("Do you want to try one more time? [Y/N]: ")
        if user_choose.lower() == 'y' or user_choose.lower() == 'yes':
            continue
        else:
            break
