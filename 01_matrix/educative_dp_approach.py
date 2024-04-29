# https://leetcode.com/problems/01-matrix/
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        - Iterate thru the matrix and check for the non-zero elements.
        - At each nonzero element, take the minimum of the element above and to its left
        and add 1 to the result. Now store the updated result to the current cell.
        - Traverse the whole matrix from the top-left element to the bottom-right element, and
        update each non-zero element using the same procedure.

        - Next, starting from bottom-right element, looking for even shorter paths to the nearest 0.
        - While iterating backward, take the minimum of the element below and to the right of the current cell
        and add 1. Let's call it the cell's "candidate distance."
        - Then, store the lower of the current cell value and its candidate distance in the current cell.
        """
        MAX_ROW, MAX_COL = len(mat), len(mat[0])

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] != 0:
                    top_elem: float = (
                        mat[row - 1][col] if row - 1 >= 0 else float("inf")
                    )
                    left_elem: float = (
                        mat[row][col - 1] if col - 1 >= 0 else float("inf")
                    )
                    mat[row][col] = min(top_elem + 1, left_elem + 1)

        for row in reversed(range(len(mat))):
            for col in reversed(range(len(mat[0]))):
                if mat[row][col] != 0:
                    bottom_elem: float = (
                        mat[row + 1][col] if row + 1 < MAX_ROW else float("inf")
                    )
                    right_elem: float = (
                        mat[row][col + 1] if col + 1 < MAX_COL else float("inf")
                    )
                    mat[row][col] = min(mat[row][col], bottom_elem + 1, right_elem + 1)

        return mat
