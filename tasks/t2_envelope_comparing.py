#!/usr/bin/env python3


def main():
    print("This program checks if it's possible to put one envelope another")
    while True:
        print("\nEnvelop number one")
        size_a, size_b = set_envelope_size()
        envelope_one = Envelope(size_a, size_b)
        print("The first envelope has been successfully created!")

        print("\nEnvelop number two")
        size_a, size_b = set_envelope_size()
        envelope_two = Envelope(size_a, size_b)
        print("The second envelope has been successfully created!\n")

        result = compare_envelopes(envelope_one, envelope_two)
        if result:
            print("You can put one envelope in another!")
        else:
            print("You can NOT put one envelope in another!")

        user_choose = input("Do you want to try one more time? [Y/N]: ")
        if not user_choose.lower() in ("y", "yes"):
            break


def set_envelope_size():
    while True:
        try:
            # vprint("Enter empty lines to exit")
            side_a = input("Enter first side: ")
            side_b = input("Enter second side: ")
            if side_a == "" and side_b == "":
                exit()
            side_a, side_b = float(side_a), float(side_b)
            if side_a <= 0 or side_b <= 0:
                raise ValueError
            return side_a, side_b
        except ValueError:
            print("You need to enter positive float values, dummy!\n")


def compare_envelopes(envelope_1, envelope_2):
    if envelope_2 < envelope_1 or envelope_1 < envelope_2:
        return True
    else:
        return False


class Envelope:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __lt__(self, other):
        if self.side_a < other.side_a and self.side_b < other.side_b:
            return True
        else:
            return False


if __name__ == "__main__":
    main()
