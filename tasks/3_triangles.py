"""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 3
"""

from tasks_opt_parsesr import *
import math


class Triangle:
    def __init__(self, name, a_size, b_size, c_size):
        """Create triangle with sides A, B, C and count it's square"""
        try:
            self.name = name
            self.side_a = float(a_size)
            self.side_b = float(b_size)
            self.side_c = float(c_size)
        except (TypeError, ValueError):
            print("Invalid input!")
            self.is_valid = False
        else:
            if self.side_a + self.side_b > self.side_c \
                    and self.side_a + self.side_c > self.side_b \
                    and self.side_c + self.side_b > self.side_a:
                self.is_valid = True
            else:
                print("Invalid size!")
                self.is_valid = False

        if self.is_valid:
            self.p = (self.side_a + self.side_b + self.side_c)/2
            self.square = math.sqrt(self.p
                                    * (self.p - self.side_a)
                                    * (self.p - self.side_b)
                                    * (self.p - self.side_c))
        else:
            print("This triangle is not valid!")

    def get_square(self):
        return self.square


if __name__ == "__main__":
    set_opts_task3()
    triangle_list = []

    while True:
        print("Enter your triangle:")
        try:
            tr_name, a_size, b_size, c_size = input("Name, side A, side B, side C: ").split()
            someTriangle = Triangle(tr_name, a_size, b_size, c_size)
        except ValueError as e:
            print(e)
        else:
            if someTriangle.is_valid:
                print("")
                triangle_list.append(someTriangle)

            user_choose = input("Do you want to add more triangles? [Y/N]: ")
            if user_choose.lower() == 'y' or user_choose.lower() == 'yes':
                continue
            else:
                break

    if triangle_list:
        triangle_list = sorted(triangle_list, key=lambda tr: tr.square, reverse=True)
        print("\n============= Triangles list: ===============")
        for index, triangle in enumerate(triangle_list):
            print(f"{index}. [{triangle.name}]: {triangle.get_square():.2f}cm")
    else:
        print("There are no triangles in this list!")
