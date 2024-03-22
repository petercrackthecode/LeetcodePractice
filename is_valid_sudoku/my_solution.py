# https://leetcode.com/problems/valid-sudoku/
from typing import List, Tuple


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        for each cell (i, j) we've traversed thru within board:
        - if the cell is already filled (board[i][j] != '.'), check if the cell's number exists:
            - vertically.
            - horizontally.
            - within the 3x3 sub array. have a function called is_valid_within_sub_array(r: int, c: int) to help you do so.
            if any condition above matches, returns False.
        - otherwise, fill the cell:
            - initialize a set of available_numbers = {x for x in range(1, 10)}
            - check if there is any number exists:
                - vertically: check all the rows sharing the column j.
                - horizontally: check all the columns sharing the row i.
                - 3x3 subarray
              if there is any number exists (cell != '.'), discard it from available_numbers
            - if the len of available_numbers is greater than 0, fill the cell with list(available_numbers)[0]
            - otherwise, return False immediately.

        return True
        """
        max_row: int = 9
        max_col: int = 9

        def get_range(num: int) -> Tuple[int, int]:
            start = end = -1

            if 0 <= num <= 2:
                start, end = 0, 2
            elif 3 <= num <= 5:
                start, end = 3, 5
            else:  # 6 -> 8
                start, end = 6, 8

            return start, end

        def is_filled_cell_valid(row: int, col: int) -> bool:
            nonlocal max_row, max_col, board
            val = board[row][col]
            # check horizontally
            for c in range(max_col):
                if board[row][c] == val and c != col:
                    print(f"failed horizontally at row = {row}, col = {c}")
                    return False
            # check vertically
            for r in range(max_row):
                if board[r][col] == val and r != row:
                    print(f"failed vertically at row = {r}, col = {col}")
                    return False
            sub_row_start, sub_row_end = get_range(row)
            sub_col_start, sub_col_end = get_range(col)

            for r in range(sub_row_start, sub_row_end + 1):
                for c in range(sub_col_start, sub_col_end + 1):
                    if board[r][c] == val and (r != row or c != col):
                        return False

            return True

        for r in range(max_row):
            for c in range(max_col):
                if board[r][c] != ".":  # filled cell
                    if not is_filled_cell_valid(r, c):
                        return False

        return True
