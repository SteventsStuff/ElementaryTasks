#!/usr/bin/env python3
import unittest
import tasks.t3_triangles as triang
from tasks.t3_triangles import Triangle


class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.triangle_1 = Triangle("tr1", 12, 15, 14)
        self.triangle_2 = Triangle("tr2", 10.5, 13.5, 12.5)
        self.triangle_3 = Triangle("tr3", 2, 5, 4)
        self.triangle_4 = Triangle("test_1", 7, 10.3, 9)

    # testing Triangle class
    def test_Triangle_constructor(self):
        self.assertEqual(("test_1", 7, 10.3, 9),
                         (self.triangle_4._name, self.triangle_4.a_size,
                          self.triangle_4.b_size, self.triangle_4.c_size))

    def test_validate_triangle_size_perfect_input(self):
        self.assertEqual(None, self.triangle_4.validate_triangle_size())

    # ???
    # def test_validate_triangle_size_incorrect_input(self):
    #     self.assertRaises(ValueError, Triangle("test_error", 7, 1, 9))

    def test_get_area(self):
        self.assertEqual(78.92678569408487, self.triangle_1.get_area())

    def test_get_name(self):
        self.assertEqual("tr3", self.triangle_3.get_name())

    # testing print func
    def test_print_triangles_empty_list(self):
        expected = "There are no triangles in this list!"
        self.assertEqual(expected, triang.print_triangles([]))

    def test_print_triangles_perfect_list(self):
        triangle_list = [self.triangle_1, self.triangle_2,
                         self.triangle_3, self.triangle_4]
        expected = """1. [tr1]: 78.93cm
2. [tr2]: 62.15cm
3. [test_1]: 30.93cm
4. [tr3]: 3.80cm
"""
        self.assertEqual(expected, triang.print_triangles(triangle_list))


if __name__ == "__main__":
    unittest.main()
