#!/usr/bin/env python3


def main():
    print("This program checks if it's possible to put one envelope another")
    while True:
        print("\nEnvelop number one")
        envelope_one = create_envelope()
        print("The first envelope has been successfully created!")

        print("\nEnvelop number two")
        envelope_two = create_envelope()
        print("The second envelope has been successfully created!\n")

        compare_envelopes(envelope_one, envelope_two)

        user_choose = input("Do you want to try one more time? [Y/N]: ")
        if not user_choose.lower() in ("y", "yes"):
            break


def print_wrong_type_message():
    return "You need to enter positive float values, dummy!\n"


def set_envelope_size():
    while True:
        try:
            print("Enter empty lines to exit")
            side_a = input("Enter first side: ")
            side_b = input("Enter second side: ")
            if side_a == "" and side_b == "":
                exit()
            side_a, side_b = float(side_a), float(side_b)
            if side_a <= 0 or side_b <= 0:
                raise ValueError
            return side_a, side_b
        except ValueError:
            print(print_wrong_type_message())


def create_envelope():
    size_a, size_b = set_envelope_size()
    envelope = Envelope(size_a, size_b)
    return envelope


def compare_envelopes(envelope_1, envelope_2):
    if envelope_2 < envelope_1 or envelope_1 < envelope_2:
        print("You can put one envelope in another!")
    else:
        print("You can NOT put one envelope in another!")


class Envelope:
    def __init__(self, side_a, side_b):
        self._side_a = side_a
        self._side_b = side_b

    def __lt__(self, other):
        if self._side_a < other.side_a and self._side_b < other.side_b:
            return True
        else:
            return False


if __name__ == "__main__":
    main()
