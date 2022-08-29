# https://leetcode.com/problems/where-will-the-ball-fall/
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        row, col = (len(grid), len(grid[0]))
        for c in range(col):
            column_iterator = c
            r = 0
            while r < row:
                if grid[r][column_iterator] == 1:
                    # to the right
                    if column_iterator+1 >= col or grid[r][column_iterator+1] == -1:
                        ans.append(-1)
                        break
                    else:
                        column_iterator += 1
                        r += 1
                elif grid[r][column_iterator] == -1:
                    # to the left
                    if column_iterator-1 < 0 or grid[r][column_iterator-1] == 1:
                        ans.append(-1)
                        break
                    else:
                        column_iterator -= 1
                        r += 1

            if r >= row:
                # We have traversed through the bottom row => the ball went through
                ans.append(column_iterator)
        return ans
