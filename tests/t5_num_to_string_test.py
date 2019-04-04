#!/usr/bin/env python3
import unittest
import argparse
from mock import patch
import tasks.t5_num_to_string as numstr


class TestNumToStr(unittest.TestCase):
    # testing args parsr
    def tests_parse_args_from_cmdline_perfect_args(self):
        args = ["--num", "10"]
        expected = argparse.Namespace(number="10")
        self.assertEqual(expected, numstr.parse_args_from_cmdline(args))

    def tests_parse_args_from_cmdline_empty_args(self):
        expected = argparse.Namespace(number="0")
        self.assertEqual(expected, numstr.parse_args_from_cmdline(""))

    # testing num2words
    def test_num2words_0_9(self):
        self.assertEqual("Five", numstr.num2words(5))

    def test_num2words_10_19(self):
        self.assertEqual("Fifteen", numstr.num2words(15))

    def test_num2words_20_90(self):
        self.assertEqual("Forty", numstr.num2words(40))

    def test_num2words_20_90_2(self):
        self.assertEqual("Forty Eight", numstr.num2words(48))

    def test_num2words_100_999(self):
        self.assertEqual("Seven Hundred Fifty Three", numstr.num2words(753))

    def test_num2words_1000_999999(self):
        self.assertEqual("Fifteen Thousand Four Hundred Sixty Seven",
                         numstr.num2words(15467))

    def test_num2words_1000_999999_2(self):
        self.assertEqual("Six Hundred Twenty Six Thousand Eight Hundred Forty Seven",
                         numstr.num2words(626847))

    def test_num2words_1000000_1000000000(self):
        expected = "One Billion Five Hundred Sixty Nine Million Eight Hundred" \
                   " Seventy Four Thousand Three Hundred Twenty One"
        self.assertEqual(expected, numstr.num2words(1569874321))

    # testing get_user_input
    def test_get_user_input_perfect_input(self):
        with patch("tasks.t5_num_to_string.input", return_value=20):
            self.assertEqual(20, numstr.get_user_input())

    def test_get_user_input_less_than_zero(self):
        with patch("tasks.t5_num_to_string.input", return_value=-20):
            self.assertEqual(-20, numstr.get_user_input())

    # def test_get_user_input_float(self):
    #     with patch("tasks.t5_num_to_string.input", return_value=2.6):
    #         self.assertRaises(ValueError, numstr.get_user_input())
    #
    # def test_get_user_input_str(self):
    #     with patch("tasks.t5_num_to_string.input", return_value="some string"):
    #         self.assertRaises(ValueError, numstr.get_user_input())


if __name__ == "__main__":
    unittest.main()
