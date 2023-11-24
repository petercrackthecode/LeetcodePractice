# https://leetcode.com/problems/maximal-square/
from collections import defaultdict
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        row = len(matrix), col = len(matrix[0])
        have a dictionary called max_square_size_from_cell (key: (r: int, c: int), value: max square size with top left edge starting from (r, c): int)
        for each cell (r, c), we can limit the number of adjacent cells we should check by checking the maximum square we can form from (r+1, c+1) (if r+1 & c+1 are within the boundary), get the size of that square from (r+1, c+1), then only check the rows & columns from r -> r + size - 1 and c -> c + size - 1
        initialize max_square_size_from_cell whose row is at the bottom of our matrix by matrix[row-1][c] (row = len(matrix), c = 0 -> col - 1)
        from the bottom to top (row - 2 -> 0, inclusively), right -> left (col - 1 -> 0, inclusively), if the diagonally down right cell (r+1, c+1) of the current cell exists:
        - no: max_square_size_from_cell[(r, c)] = matrix[r][c]
        - yes: check_range = max_square_size_from_cell[(r+1, c+1)]
            from the current cell, check on the right side of the cell check_range times (c+1 -> c + check_range), if the values on the right are all 1, count those values (count_right) & continue to checking at the bottom. otherwise, stop.
            from the current cell, check on the bottom side of the cell check_range times (r + 1 -> r + check_ranges). if all the values at the bottom are 1, count those values (count_bottom) assign max_square_size = max(max_square_size, check_ranges + 1). 
                max_square_size_from_cell[(r, c)] = 1 + min(count_right, count_bottom, max_square_size_from_cell[(r+1, c+1)])

        return max_square_size * max_square_size
        """
        max_square_size = 0
        max_square_size_from_cell = defaultdict(int)
        row, col = len(matrix), len(matrix[0])

        # initialize bottom cells
        for c in range(col):
            max_square_size_from_cell[(row-1, c)] = int(matrix[row-1][c])
            if max_square_size_from_cell[(row-1, c)] > max_square_size:
                max_square_size = max_square_size_from_cell[(row-1, c)]
        # initialize right cells
        for r in range(row):
            max_square_size_from_cell[(r, col-1)] = int(matrix[r][col-1])
            if max_square_size_from_cell[(r, col-1)] > max_square_size:
                max_square_size = max_square_size_from_cell[(r, col-1)]

        for r in reversed(range(row-1)):
            for c in reversed(range(col-1)):
                if matrix[r][c] == '0':
                    max_square_size_from_cell[(r, c)] = 0
                elif max_square_size_from_cell[(r+1, c+1)] == 0:
                    # matrix[r][c] == '1'
                    max_square_size_from_cell[(r, c)] = 1
                else:
                    # matrix[r][c] == '1' and max_square_size_from_cell[(r+1, c+1)] >= 1
                    count_right = max_square_size_from_cell[(r, c + 1)]
                    count_bottom = max_square_size_from_cell[(r + 1, c)]
                    max_square_size_from_cell[(
                        r, c)] = 1 + min(count_right, count_bottom, max_square_size_from_cell[(r+1, c+1)])
                max_square_size = max(
                    max_square_size, max_square_size_from_cell[(r, c)])

        return max_square_size * max_square_size
