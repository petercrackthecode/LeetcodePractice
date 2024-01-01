# https://leetcode.com/problems/leftmost-column-with-at-least-a-one

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        rst = m

        for i in range(n):
            lo, hi = 0, m
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if binaryMatrix.get(i, mid) < 1:
                    lo = mid + 1
                else:
                    hi = mid
            rst = min(hi, rst)

        return rst if rst < m else -1
