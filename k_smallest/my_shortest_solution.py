# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
from typing import List
from functools import reduce


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        matrix = [
            [1, 5, 9 ],
            [10,11,13],
            [12,13,15]
        ]
        bruteforce:
        - convert matrix to a 1D array and save the output to matrix.
        - sort matrix
        - return matrix[k-1]
        """
        matrix = reduce(lambda l1, l2: l1 + l2, matrix, [])

        matrix.sort()

        return matrix[k - 1]
