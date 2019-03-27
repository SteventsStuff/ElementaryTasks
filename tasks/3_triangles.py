"""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 3
"""

import math


def main():
    print("This program counts areas of N triangles and prints them into"
          " a console, sorted by their areas\n")
    triangle_list = []

    while True:
        print("Enter triangle: ")
        try:
            tr_name, a_size, b_size, c_size = input("Name, sides A, B, C: ").split()
            # a_size, b_size, c_size = float(a_size), float(b_size), float(c_size)
            triangle_instance = Triangle(tr_name, float(a_size), float(b_size), float(c_size))
        except (ValueError, TypeError) as e:
            print(e)
        else:
            triangle_list.append(triangle_instance)
            print("Triangle added to the list")

        user_choose = input("Do you want to add more triangles? [Y/N]: ")
        if user_choose.lower() == 'y' or user_choose.lower() == 'yes':
            continue
        else:
            break

    print_triangles(triangle_list)


def print_triangles(triangle_list):
    if triangle_list:
        triangle_list = sorted(triangle_list, key=lambda tr: tr.get_square(), reverse=True)
        print("\n============= Triangles list: ===============")
        for index, triangle in enumerate(triangle_list):
            print(f"{index+1}. [{triangle.get_name()}]: {triangle.get_square():.2f}cm")
    else:
        print("There are no triangles in this list!")


class Triangle:
    def __init__(self, name, a_size, b_size, c_size):
        """Create triangle with sides A, B, C and count it's square"""
        self.name = name
        self.a_size = a_size
        self.b_size = b_size
        self.c_size = c_size

        self.check_is_valid()
        self.square = self.calc_square()

    def check_is_valid(self):
        if not (self.a_size + self.b_size > self.c_size
                and self.a_size + self.c_size > self.b_size
                and self.c_size + self.b_size > self.a_size):
            raise ValueError("Invalid size!")

    def calc_square(self):
        p = (self.a_size + self.b_size + self.c_size) / 2
        return math.sqrt(p
                         * (p - self.a_size)
                         * (p - self.b_size)
                         * (p - self.c_size))

    def get_square(self):
        return self.square

    def get_name(self):
        return self.name


if __name__ == "__main__":
    main()
