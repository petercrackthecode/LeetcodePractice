# https://leetcode.com/problems/design-tic-tac-toe/
from typing import List


class TicTacToe:

    def __init__(self, n: int):
        self.board_size: int = n
        # n rows: 0 -> n-1
        self.row: List[int] = [0 for _ in range(n)]
        # n columns: 0 -> n-1
        self.col: List[int] = [0 for _ in range(n)]
        # two diagonal lines:
        #   - top left -> bottom right: row == column (self.diagonal[0])
        #   - bottom left -> top right: row + column == self.board_size - 1 (self.diagonal[1])
        self.diagonal: List[int] = [0 for _ in range(2)]

    """
    n=3
        0 1 2
        _____
    0   0 0 0
    1   0 0 0
    2   0 0 0
    """

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            self.diagonal[0] = (self.diagonal[0] + 1) if row == col else self.diagonal[0]
            self.diagonal[1] = (
                (self.diagonal[1] + 1) if (row + col == self.board_size - 1) else self.diagonal[1]
            )

            if (
                abs(self.row[row]) == self.board_size
                or abs(self.col[col]) == self.board_size
                or abs(self.diagonal[0]) == self.board_size
                or abs(self.diagonal[1]) == self.board_size
            ):
                # player 1 won
                return 1
        else:  # player == 2
            self.row[row] -= 1
            self.col[col] -= 1
            self.diagonal[0] = (self.diagonal[0] - 1) if row == col else self.diagonal[0]
            self.diagonal[1] = (
                (self.diagonal[1] - 1) if (row + col == self.board_size - 1) else self.diagonal[1]
            )

            if (
                abs(self.row[row]) == self.board_size
                or abs(self.col[col]) == self.board_size
                or abs(self.diagonal[0]) == self.board_size
                or abs(self.diagonal[1]) == self.board_size
            ):
                # player 2 won
                return 2

        return 0
