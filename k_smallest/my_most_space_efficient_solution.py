# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        matrix = [
            [1, 5, 9 ],
            [10,11,13],
            [12,13,15]
        ]
        - loop n-1 times:
            - pop the last row in matrix.
            - add that popped row to the first row
        - sort the first row: matrix[0].sort()
        - return the kth element in the first row: return matrix[0][k-1]
        """
        n = len(matrix)
        for _ in range(n - 1):
            matrix[0].extend(matrix.pop())

        matrix[0].sort()

        return matrix[0][k - 1]
