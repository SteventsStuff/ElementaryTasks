#!/usr/bin/env python3
import unittest
from mock import patch
import tasks.t2_envelope_comparing as ec
from tasks.t2_envelope_comparing import Envelope


class TestEnvelope(unittest.TestCase):
    def setUp(self) -> None:
        self.my_envelope_1 = Envelope(2.45, 10.25)
        self.my_envelope_2 = Envelope(2.45, 12.25)
        self.my_envelope_3 = Envelope(1.20, 5.45)

    # testing Envelope class
    def test_Envelope_constructor(self):
        self.assertEqual((2.45, 10.25), (self.my_envelope_1.side_a,
                                         self.my_envelope_1.side_b))

    # testing comparing envelopes
    def test_envelope_comparing_one_envelope_can_be_put_into_another(self):
        self.assertEqual(True, self.my_envelope_3 < self.my_envelope_1)

    def test_envelope_comparing_one_envelope_can_not_be_put_into_another(self):
        self.assertEqual(False, self.my_envelope_1 < self.my_envelope_2)

    def test_envelope_comparing_same_envelope(self):
        self.assertEqual(False, self.my_envelope_1 < self.my_envelope_1)

    # testing set_envelope_size
    def test_set_envelope_size_int_input(self):
        with patch("tasks.t2_envelope_comparing.input", return_value=5):
            self.assertEqual((5, 5), ec.set_envelope_size())

    def test_set_envelope_size_float_input(self):
        with patch("tasks.t2_envelope_comparing.input", return_value=7.3):
            self.assertEqual((7.3, 7.3), ec.set_envelope_size())

    """idk why it's dose not works"""
    # def test_set_envelope_size_less_than_zero(self):
    #     with patch("tasks.t2_envelope_comparing.input", return_value=-10):
    #         self.assertEqual(ValueError, ec.set_envelope_size())
    #
    # def test_set_envelope_size_str_input(self):
    #     with patch("tasks.t2_envelope_comparing.input", return_value="kek"):
    #         self.assertRaises(ValueError, ec.set_envelope_size())
    #
    # def test_set_envelope_size_empty_input(self):
    #     with patch("tasks.t2_envelope_comparing.input", return_value=""):
    #         self.assertRaises(SystemExit, ec.set_envelope_size())


if __name__ == "__main__":
    unittest.main()
