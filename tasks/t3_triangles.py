#!/usr/bin/env python3
import math


def main():
    print("This program counts areas of N triangles and prints them into"
          " a console, sorted by their areas\n")
    triangle_list = []

    while True:
        try:
            name, a_size, b_size, c_size = input("Name, A, B, C: ").split()
            triangle_instance = Triangle(name,
                                         float(a_size),
                                         float(b_size),
                                         float(c_size))
            triangle_instance.get_area()
        except ValueError:
            print("Invalid input!\nThis triangle won't be added to the list!\n")
        else:
            triangle_list.append(triangle_instance)
            print("Triangle added to the list")

        user_choose = input("Do you want to add more triangles? [Y/N]: ")
        if not user_choose.lower() in ("y", "yes"):
            break

    print("\n============== Triangles list: ================")
    res_list = print_triangles(triangle_list)
    print(res_list)


def print_triangles(triangle_list):
    res_list = ""
    if triangle_list:
        triangle_list = sorted(triangle_list,
                               key=lambda triangle: triangle.get_area(),
                               reverse=True)
        for index, tr in enumerate(triangle_list):
            res_list += f"{index+1}. [{tr.get_name()}]: {tr.get_area():.2f}cm\n"
        return res_list
    else:
        return "There are no triangles in this list!"


class Triangle:
    def __init__(self, name, a_size, b_size, c_size):
        self._name = name
        self.a_size = a_size
        self.b_size = b_size
        self.c_size = c_size
        self.validate_triangle_size()

    def validate_triangle_size(self):
        if not (self.a_size + self.b_size > self.c_size
                and self.a_size + self.c_size > self.b_size
                and self.c_size + self.b_size > self.a_size):
            raise ValueError

    def get_area(self):
        p = (self.a_size + self.b_size + self.c_size) / 2
        return math.sqrt(p
                         * (p - self.a_size)
                         * (p - self.b_size)
                         * (p - self.c_size))

    def get_name(self):
        return self._name


if __name__ == "__main__":
    main()
