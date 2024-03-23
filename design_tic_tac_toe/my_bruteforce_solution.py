# https://leetcode.com/problems/design-tic-tac-toe/description/
from typing import List


class TicTacToe:
    """
    - 2 players:
        - player 1: O: 1
        - player 2: X: 2
    - have a 2d array of values 0, 1, 2: board: List[List[int]]
        - 0 means unfilled.
        - 1 means O
        - 2 means X
    - after each move executes the 3 check functions:
        - check horizontally: check if any of the rows are homogenous (all O or all X). have a helper function called check_horizontal() -> int to help us do so.
        - check vertically: check if any of the columns are homogenous (all O or all X). have a helper function called check_vertically() -> int to help us do so.
        - check two diagonal lines: check if two diagonal lines are homogenous (all O or all X). have a helper function call check_diagonal() -> int to help us do so.
    """

    def __init__(self, n: int):
        self.board: List[List[int]] = [[0 for __ in range(n)] for _ in range(n)]

    def check_horizontally(self) -> int:
        # check rows
        for r in range(len(self.board)):
            # check all the columns if they are homogenous and not 0
            has_winner: bool = True
            for c in range(1, len(self.board[0])):
                if (
                    self.board[r][c - 1] == 0
                    or self.board[r][c] == 0
                    or self.board[r][c] != self.board[r][c - 1]
                ):
                    has_winner = False
                    break
            # found a valid row
            if has_winner:
                # print('won horizontally')
                # print(f'row = {r}, col = {c}')
                # print(f'self.board = {self.board}')
                return self.board[r][c]

        return 0

    def check_vertically(self) -> int:
        for c in range(len(self.board[0])):
            has_winner: bool = True
            for r in range(1, len(self.board)):
                if (
                    self.board[r][c] == 0
                    or self.board[r - 1][c] == 0
                    or self.board[r][c] != self.board[r - 1][c]
                ):
                    has_winner = False
                    break
                # found a valid column
            if has_winner:
                # print('won vertically')
                # print(f'self.board = {self.board}')
                return self.board[r][c]
        return 0

    def check_diagonally(self) -> int:
        """
        |X| | |
        | | | |    // Player 1 makes a move at (0, 0).
        | | | |
        """
        # top left -> bottom right
        row = col = 1
        has_winner: bool = True
        while row < len(self.board) and col < len(self.board[0]):
            prev_cell = self.board[row - 1][col - 1]
            curr_cell = self.board[row][col]
            if prev_cell == 0 or curr_cell == 0 or prev_cell != curr_cell:
                has_winner = False
                break
            row += 1
            col += 1

        if has_winner:
            return self.board[0][0]

        # bottom left -> top right
        row = len(self.board) - 1
        col = 0

        has_winner = True

        while row > 0 and col < len(self.board[0]) - 1:
            curr_cell = self.board[row][col]
            next_cell = self.board[row - 1][col + 1]
            if next_cell == 0 or curr_cell == 0 or next_cell != curr_cell:
                has_winner = False
                break
            row -= 1
            col += 1
        if has_winner:
            return self.board[len(self.board) - 1][0]

        return 0

    """
    returns:
    - 0 if no winner after the move
    - 1 if player 1 won.
    - 2 if player 2 won
    """

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        # print(f'\nself.board = {self.board}')
        return self.check_horizontally() or self.check_vertically() or self.check_diagonally()
        """
        2
        
        0 1
        1 2
        """
