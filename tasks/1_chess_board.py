"""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 1
"""

from tasks_opt_parsesr import *


class ChessBoard:
    def __init__(self, width, height):
        """This class create chess board.
        Fields:
            __width: int
            __height: int
        Methods:
            draw_board() :return: str

        If constructor has invalid inputs (can not convert
        width or height to integer, then its stars Interactive mode)
        """
        self.IM_flag = False
        while True:
            try:
                if self.IM_flag:
                    self.__height = int(input("Enter width: "))
                    self.__width = int(input("Enter height: "))
                else:
                    self.__height = int(height)
                    self.__width = int(width)

                if self.__width < 1 or self.__height < 1:
                    print("Invalid size!")
                    raise ValueError

            except (TypeError, ValueError):
                print("Interactive mode:")
                self.IM_flag = True
            else:
                break

    def draw_board(self):
        """Draw chess board.
        Returns:
            string that visualizes a chess board
        """
        board_str = ""
        for h in range(1, self.__height + 1):
            for elem in range(h,  self.__width + h):
                if elem % 2 == 0:
                    board_str += " "
                else:
                    board_str += "*"
            board_str += "\n"

        return board_str[:-1]


if __name__ == "__main__":
    opts = set_opts_task1()
    print(ChessBoard(opts[0], opts[1]).draw_board())
