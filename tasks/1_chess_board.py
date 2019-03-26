"""
Group:      DP158Py
Student:    Miroshnychenko V.
Task:       Task 1
"""

import tasks_opt_parsesr


class ChessBoard:
    def __init__(self, width, height):
        """Create chess board with size width * height"""
        self.width = width
        self.height = height

    def draw_board(self):
        """Draw a chess board"""
        board_str = ""
        for h in range(1, self.height + 1):
            for elem in range(h,  self.width + h):
                if elem % 2 == 0:
                    board_str += " "
                else:
                    board_str += "*"
            board_str += "\n"

        return board_str[:-1]


if __name__ == "__main__":
    opts = tasks_opt_parsesr.parse_task1_options()
    print(ChessBoard(opts[0], opts[1]).draw_board())
