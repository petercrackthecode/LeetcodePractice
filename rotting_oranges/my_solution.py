# https://leetcode.com/problems/rotting-oranges/
from collections import deque
from typing import List


def is_fresh(grid: List[List[int]], row: int, col: int) -> bool:
    MAX_ROW = len(grid) - 1
    MAX_COL = len(grid[0]) - 1
    if (row < 0) or (row > MAX_ROW) or (col < 0) or (col > MAX_COL):
        return False

    return grid[row][col] == 1


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Have a queue to save the rotten oranges that we haven't gone through by each minutes. call it rotten_oranges.
        By each minute, consecutively popped the rotten oranges from the queue, check if 4-directionally adjacent oranges to that popped orange are fresh. If they are, make them rotten and add them to the queue.

        We should keep track of the fresh oranges remaining => have a variable called remaining_fresh_oranges = 0
        Iterate through our grid to count the number of remaining_fresh_oranges & append all the cells where cell[row][col] == 2 (there's a rotten orange in that cell) to our rotten_oranges queue.

        + Have two queues, one is rotten_oranges (to save the cells that contain the oranges that already rotten), other is freshly_rotten_oranges (to save the cells that contain the oranges which are just freshly contaminated).
        + While rotten_oranges or freshly_rotten_oranges is not empty, do the following operations:
            - if rotten_oranges is empty:
                rotten_oranges = freshly_rotten_oranges
                freshly_rotten_oranges.clear()
            - otherwise:
                elapsed_minutes += 1
                exhaust the rotten_oranges queue, and each time we get a rotten orange, check if the cells that are 4-directionally adjacent to that cell contain any fresh oranges.
                if yes, rotten them (assign the cell to 2), then push the cell's (x,y) position to the freshly_rotten_oranges queue, then decrease remaining_fresh_oranges by 1.

        In the end, if remaining_fresh_oranges > 0: return -1
        else: return elapsed_minutes
        """

        elapsed_minutes = 0
        remaining_fresh_oranges = 0
        rotten_oranges = deque()
        freshly_rotten_oranges = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    remaining_fresh_oranges += 1
                elif grid[row][col] == 2:
                    rotten_oranges.append((row, col))

        while len(rotten_oranges) != 0 or len(freshly_rotten_oranges) != 0:
            if len(rotten_oranges) == 0:
                elapsed_minutes += 1
                rotten_oranges = deque(freshly_rotten_oranges)
                freshly_rotten_oranges.clear()
            else:
                # len(freshly_rotten_oranges) > 0
                while len(rotten_oranges) > 0:
                    (row, col) = rotten_oranges.popleft()
                    # check fresh orange top:
                    if is_fresh(grid, row - 1, col):
                        grid[row-1][col] = 2
                        freshly_rotten_oranges.append((row-1, col))
                        remaining_fresh_oranges -= 1

                    # check fresh orange left:
                    if is_fresh(grid, row, col - 1):
                        grid[row][col-1] = 2
                        freshly_rotten_oranges.append((row, col-1))
                        remaining_fresh_oranges -= 1

                    # check fresh orange right:
                    if is_fresh(grid, row, col+1):
                        grid[row][col+1] = 2
                        freshly_rotten_oranges.append((row, col+1))
                        remaining_fresh_oranges -= 1

                    # check fresh orange bottom:
                    if is_fresh(grid, row+1, col):
                        grid[row+1][col] = 2
                        freshly_rotten_oranges.append((row+1, col))
                        remaining_fresh_oranges -= 1
        return -1 if remaining_fresh_oranges > 0 else elapsed_minutes
