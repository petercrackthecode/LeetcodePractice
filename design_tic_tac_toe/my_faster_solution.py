# https://leetcode.com/problems/design-tic-tac-toe/
from typing import List, Set, Tuple


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
        # for each row, Each set represents a set of columns filled with 1
        self.player_1_horizontal_lines: List[Set[int]] = [set() for _ in range(n)]
        # for each column, Each set represents a set of rows filled with 1
        self.player_1_vertical_lines: List[Set[int]] = [set() for _ in range(n)]

        # for each row, Each set represents a set of columns filled with 2
        self.player_2_horizontal_lines: List[Set[int]] = [set() for _ in range(n)]
        # for each column, Each set represents a set of rows filled with 2
        self.player_2_vertical_lines: List[Set[int]] = [set() for _ in range(n)]

        self.top_left_bottom_right_player_1: Set[Tuple[int, int]] = set()
        self.bottom_left_top_right_player_1: Set[Tuple[int, int]] = set()

        self.top_left_bottom_right_player_2: Set[Tuple[int, int]] = set()
        self.bottom_left_top_right_player_2: Set[Tuple[int, int]] = set()

        row: int = 0
        col: int = 0

        while row < n and col < n:
            self.top_left_bottom_right_player_1.add((row, col))
            self.top_left_bottom_right_player_2.add((row, col))
            row += 1
            col += 1

        row = n - 1
        col = 0
        while row >= 0 and col < n:
            self.bottom_left_top_right_player_1.add((row, col))
            self.bottom_left_top_right_player_2.add((row, col))
            row -= 1
            col += 1

    """
    returns:
    - 0 if no winner after the move
    - 1 if player 1 won.
    - 2 if player 2 won
    """

    def move(self, row: int, col: int, player: int) -> int:
        n: int = len(self.board)
        self.board[row][col] = player

        if player == 1:
            self.player_1_horizontal_lines[row].add(col)
            self.player_1_vertical_lines[col].add(row)
            self.top_left_bottom_right_player_1.discard((row, col))
            self.bottom_left_top_right_player_1.discard((row, col))

            if (
                len(self.player_1_horizontal_lines[row]) == n
                or len(self.player_1_vertical_lines[col]) == n
                or len(self.top_left_bottom_right_player_1) == 0
                or len(self.bottom_left_top_right_player_1) == 0
            ):
                return 1
        else:  # player == 2
            self.player_2_horizontal_lines[row].add(col)
            self.player_2_vertical_lines[col].add(row)
            self.top_left_bottom_right_player_2.discard((row, col))
            self.bottom_left_top_right_player_2.discard((row, col))

            # print(f'self.top_left_bottom_right_player_2 = {self.top_left_bottom_right_player_2}')
            # print(f'self.bottom_left_top_right_player_2 = {self.bottom_left_top_right_player_2}')

            if (
                len(self.player_2_horizontal_lines[row]) == n
                or len(self.player_2_vertical_lines[col]) == n
                or len(self.top_left_bottom_right_player_2) == 0
                or len(self.bottom_left_top_right_player_2) == 0
            ):
                return 2

        # print(f'\nself.board = {self.board}')
        return 0
        """
        [0,0,2],[0,1,1],[1,1,2]]
             0 1
             ___
        0    2 1
        1    0 2
        """
