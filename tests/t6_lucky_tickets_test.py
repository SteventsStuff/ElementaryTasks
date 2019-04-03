#!/usr/bin/env python3
import unittest
from mock import patch, mock_open
import argparse
import tasks.t6_lucky_tickets as lt


class LuckyTicketsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ticket_list = ["998327", "984984", "002268", "123123", "202268",
                            "546654", "010000", "159846", "325684", "258179"]
        self.file_path = "../tasks/tickets.txt"

    # arguments parser test
    def test_parse_args_from_cmdline_has_two_args(self):
        expected = argparse.Namespace(file_path="test.txt")
        args = ["--file", "test.txt"]
        self.assertEqual(expected, lt.parse_args_from_cmdline(args))

    def test_parse_args_from_cmdline_has_two_args_2(self):
        expected = argparse.Namespace(file_path="dummy_name_ldslfkls.txt")
        args = ["--file", "dummy_name_ldslfkls.txt"]
        self.assertEqual(expected, lt.parse_args_from_cmdline(args))

    def test_parse_args_from_cmdline_has_only_key(self):
        expected = argparse.Namespace(file_path="")
        args = ["--file", ""]
        self.assertEqual(expected, lt.parse_args_from_cmdline(args))

    def test_parse_args_from_cmdline_has_no_args(self):
        expected = argparse.Namespace(file_path="")
        self.assertEqual(expected, lt.parse_args_from_cmdline(""))

    # count tickets testing
    def test_count_tickets_method_piter(self):
        expected = 4
        self.assertEqual(expected, lt.count_tickets("piter", self.ticket_list)[0])

    def test_count_tickets_method_moscow(self):
        expected = 3
        self.assertEqual(expected, lt.count_tickets("moscow", self.ticket_list)[0])

    def test_count_tickets_wrong_method(self):
        expected = 0
        self.assertEqual(expected, lt.count_tickets("dummy", self.ticket_list)[0])

    # testing file parse
    @patch("tasks.t6_lucky_tickets.open", mock_open(read_data="moscow"))
    def test_get_file_content_moscow_result(self):
        self.assertEqual("moscow", lt.get_file_content(self.file_path))

    @patch("tasks.t6_lucky_tickets.open", mock_open(read_data="piter"))
    def test_get_file_content_piter_result(self):
        self.assertEqual("piter", lt.get_file_content(self.file_path))

    @patch("tasks.t6_lucky_tickets.open", mock_open(read_data="some dummy line..."))
    def test_get_file_content_wrong_result(self):
        self.assertEqual("", lt.get_file_content(self.file_path))

    # testing interactive mode
    def test_get_user_input_method_moscow_inout(self):
        with patch("tasks.t6_lucky_tickets.input", return_value="moscow"):
            self.assertEqual("moscow", lt.get_user_input_method())

    def test_get_user_input_method_piter_inout(self):
        with patch("tasks.t6_lucky_tickets.input", return_value="piter"):
            self.assertEqual("piter", lt.get_user_input_method())

    def test_get_user_input_method_empty_inout(self):
        with patch("tasks.t6_lucky_tickets.input", return_value=""):
            self.assertRaises(SystemExit, lt.get_user_input_method)
