#!/usr/bin/env python3

import math


def main():
    print("This program counts areas of N triangles and prints them into"
          " a console, sorted by their areas\n")
    triangle_list = []

    while True:
        try:
            name, a_size, b_size, c_size = input("Enter Name, A, B, C: ").split()
            triangle_instance = Triangle(name,
                                         float(a_size),
                                         float(b_size),
                                         float(c_size))
            triangle_instance.get_area()
        except ValueError:
            print("Invalid input!")
            print("This triangle won't be appended to the list!\n")
        else:
            triangle_list.append(triangle_instance)
            print("Triangle added to the list")

        user_choose = input("Do you want to add more triangles? [Y/N]: ")
        if not user_choose.lower() in ("y", "yes"):
            break

    print_triangles(triangle_list)


def print_triangles(triangle_list):
    if triangle_list:
        triangle_list = sorted(triangle_list,
                               key=lambda triangle: triangle.get_area(),
                               reverse=True)
        print("\n============= Triangles list: ===============")
        for index, tr in enumerate(triangle_list):
            print(f"{index+1}. [{tr.get_name()}]: {tr.get_area():.2f}cm")
    else:
        print("There are no triangles in this list!")


class Triangle:
    def __init__(self, name, a_size, b_size, c_size):
        """Create triangle with sides A, B, C and count it's square"""
        self.validate_triangle_size()
        self._name = name
        self._a_size = a_size
        self._b_size = b_size
        self._c_size = c_size

    def validate_triangle_size(self):
        if not (self._a_size + self._b_size > self._c_size
                and self._a_size + self._c_size > self._b_size
                and self._c_size + self._b_size > self._a_size):
            raise ValueError

    def get_area(self):
        p = (self._a_size + self._b_size + self._c_size) / 2
        return math.sqrt(p
                         * (p - self._a_size)
                         * (p - self._b_size)
                         * (p - self._c_size))

    def get_name(self):
        return self._name


if __name__ == "__main__":
    main()
