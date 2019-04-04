#!/usr/bin/env python3
import unittest
from mock import patch
import tasks.t8_fibonacci_numbers as fib


class TestFibonacciSequence(unittest.TestCase):
    # arguments parser test
    def test_parse_args_from_cmdline_perfect_args(self):
        expected = ("10", "120")
        args = ["--min", "10", "--max", "120"]
        self.assertEqual(expected, fib.parse_args_from_cmdline(args))

    def test_parse_args_from_cmdline_empty_args(self):
        expected = (None, None)
        self.assertEqual(expected, fib.parse_args_from_cmdline(""))

    def test_parse_args_from_cmdline_amy_args(self):
        expected = ("-10", "1.2")
        args = ["--min", "-10", "--max", "1.2"]
        self.assertEqual(expected, fib.parse_args_from_cmdline(args))

    # testing fibonacci_seq
    def test_fibonacci_seq(self):
        self.assertEqual("<class 'generator'>", str(type(fib.fibonacci_seq())))

    # testing user input
    # def test_get_user_input_int(self):
    #     with patch('tasks.t8_fibonacci_numbers.input', return_value=10):
    #         self.assertEqual((10, 10), fib.get_user_input())

    # def test_get_user_input_float(self):
    #     with patch('tasks.t8_fibonacci_numbers.input', return_value=122.1):
    #         self.assertEqual((122.1, 122.1), fib.get_user_input())
    #
    # def test_get_user_input_str(self):
    #     with patch('tasks.t8_fibonacci_numbers.input', return_value="heh"):
    #         self.assertRaises(ValueError, fib.get_user_input())
    #
    # def test_get_user_input_empty(self):
    #     with patch('tasks.t8_fibonacci_numbers.input', return_value=""):
    #         self.assertRaises(SystemError, fib.get_user_input())


if __name__ == "__main__":
    unittest.main()
