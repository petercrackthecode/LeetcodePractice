# https://leetcode.com/problems/rotting-oranges/
from typing import Deque, Tuple, List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        - Have a variable called oranges_count = 0
        - Have a deque as a queue of tuples called not_spreaded_rotten_oranges where each tuple is a position (row, column) of a rotten orange which hasn't spreaded to any nearby fresh orange.
        - Iterate through our grid, calculate the total number of oranges & initialize not_spreaded_rotten_oranges:
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    current_orange_status = grid[row][col]
                    if current_orange_status == 1 or current_orange_status == 2:
                        oranges_count += 1
                        if current_orange_status == 2:
                            not_spreaded_rotten_oranges.append((row, col))
        - Have a variable called unchecked_oranges = oranges_count
        - loop within not_spreaded_rotten_oranges while the queue is not empty:
            unchecked_rotten_oranges = deque()
            elapsed_time = 0
            while len(not_spreaded_rotten_oranges) > 0 or len(unchecked_rotten_oranges) > 0:
                while len(not_spreaded_rotten_oranges) > 0:
                    (r, c) = not_spreaded_rotten_oranges.popleft()
                    unchecked_oranges -= 1
                    spread_the_rot(r, c, unchecked_rotten_oranges)

                elapsed_time += 1
                not_spreaded_rotten_oranges = unchecked_rotten_oranges
                unchecked_rotten_oranges.clear()
        - return -1 if (unchecked_oranges > 0) else elapsed_time
        """
        oranges_count = 0
        not_spreaded_rotten_oranges = deque()
        unchecked_rotten_oranges = deque()
        elapsed_time = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_orange_status = grid[row][col]
                if current_orange_status == 1 or current_orange_status == 2:
                    oranges_count += 1
                    if current_orange_status == 2:
                        not_spreaded_rotten_oranges.append((row, col))

        unchecked_oranges = oranges_count

        def spread_the_rot(r: int, c: int, unchecked_rotten_oranges: Deque[Tuple[int, int]]) -> None:
            [row, col] = [len(grid), len(grid[0])]
            spreaded = False

            # spread top:
            if r > 0 and grid[r-1][c] == 1:
                grid[r-1][c] = 2
                unchecked_rotten_oranges.append((r-1, c))
                spreaded = True
            # spread left:
            if c > 0 and grid[r][c-1] == 1:
                grid[r][c-1] = 2
                unchecked_rotten_oranges.append((r, c-1))
                spreaded = True
            # spread right:
            if c < col - 1 and grid[r][c+1] == 1:
                grid[r][c+1] = 2
                unchecked_rotten_oranges.append((r, c+1))
                spreaded = True
            # spread bottom:
            if r < row - 1 and grid[r+1][c] == 1:
                grid[r+1][c] = 2
                unchecked_rotten_oranges.append((r+1, c))
                spreaded = True

            return spreaded

        while len(not_spreaded_rotten_oranges) > 0 or len(unchecked_rotten_oranges) > 0:
            spreaded = False
            while len(not_spreaded_rotten_oranges) > 0:
                (r, c) = not_spreaded_rotten_oranges.popleft()
                unchecked_oranges -= 1
                if spread_the_rot(r, c, unchecked_rotten_oranges):
                    spreaded = True

            # only increase the time if there is spread happened.
            elapsed_time += (1 if spreaded else 0)
            not_spreaded_rotten_oranges = deque(unchecked_rotten_oranges)
            unchecked_rotten_oranges.clear()

        return -1 if (unchecked_oranges > 0) else elapsed_time


grid = [[2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]]
ans = Solution().orangesRotting(grid)
print('ans = ', ans)
