# https://leetcode.com/problems/maximal-square/
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Bruteforce solution
        row = len(matrix)
        col = len(matrix[0])
        max_area = 0
        Check through all the squares row by row (r = 0 -> row - 1), column by column (c = 0 -> col - 1): For each square, if the square is 0, skip to the next square. if the square is 1. Consider the square is the top left edge of our larger square (starting with the size = 1), then keep extending the square size (in the left and bottom direction) while all the internal cells are 1 (have a helper function called largest_square_area_from_cell(r, c) to help you do so).
        compare the said result (largest_square_area_from_cell(r, c)) to max_area, and assign the max value to max_area.

        return max_area
        """
        max_area = 0
        [max_row, max_col] = [len(matrix), len(matrix[0])]

        def largest_square_area_from_cell(r: int, c: int) -> int:
            nonlocal matrix, max_row, max_col
            curr_size = 1
            next_row = r + 1
            next_col = c + 1
            while next_row < max_row and next_col < max_col:
                can_extend = True
                # check right edge
                for curr_row in range(r, next_row + 1):
                    if matrix[curr_row][next_col] == "0":
                        can_extend = False
                        break
                # check bottom edge
                for curr_col in range(c, next_col + 1):
                    if matrix[next_row][curr_col] == "0":
                        can_extend = False
                        break
                if can_extend:
                    curr_size += 1
                    next_row += 1
                    next_col += 1
                else:
                    break

            return curr_size * curr_size

        for r in range(max_row):
            for c in range(max_col):
                if matrix[r][c] == "1":
                    curr_max_area = largest_square_area_from_cell(r, c)
                    max_area = max(max_area, curr_max_area)

        return max_area
