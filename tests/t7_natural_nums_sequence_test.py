#!/usr/bin/env python3
import unittest
import argparse
from mock import patch
import tasks.t7_natural_nums_sequence as ns


class TestSequence(unittest.TestCase):
    # arguments parser test
    def test_parse_args_from_cmdline_perfect_args(self):
        expected = argparse.Namespace(number="10")
        args = ["--number", "10"]
        self.assertEqual(expected, ns.parse_args_from_cmdline(args))

    def test_parse_args_from_cmdline_empty(self):
        expected = argparse.Namespace(number=None)
        self.assertEqual(expected, ns.parse_args_from_cmdline(""))

    # testing get_sequence
    def test_get_sequence(self):
        self.assertEqual([1, 2, 3], ns.get_sequence(10))

    # testing get_user_input
    def test_get_user_input(self):
        with patch("tasks.t7_natural_nums_sequence.input", return_value=20):
            self.assertEqual(20, ns.get_user_input())

    # def test_get_user_input_empty(self):
    #     with patch("tasks.t7_natural_nums_sequence.input", return_value=""):
    #         self.assertRaises(SystemExit, ns.get_user_input())
    #
    # def test_get_user_input_float(self):
    #     with patch("tasks.t7_natural_nums_sequence.input", return_value=2.5):
    #         self.assertRaises(ValueError, ns.get_user_input())
    #
    # def test_get_user_input_str(self):
    #     with patch("tasks.t7_natural_nums_sequence.input", return_value="heh"):
    #         self.assertRaises(ValueError, ns.get_user_input())


if __name__ == "__main__":
    unittest.main()
