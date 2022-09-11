# https://leetcode.com/problems/01-matrix/
from collections import deque
from typing import List


def calculate_nearest_zero_distance(zero_distance_mat: List[List[int]], r: int, c: int, nearest_distance, assigned_value_cells: deque) -> None:
    zero_distance_mat[r][c] = nearest_distance + 1
    assigned_value_cells.append((r, c))


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Algorithm in general: initialize a queue with cells that have the mattrix values equal to zero, then concurrently popped elements from that queue
        and assigned the cells at position top([i-1][j]), right([i][j+1]), bottom([i+1][j]), left([i][j-1]) with the value cell[i][j] + 1 if the cell
        at those position haven't been initialized, then add those position to our queue.

        + In hindsight, we sweep through all cells starting with values zeroes, then assign all adjacent cell the value 1 should they haven't been initialized
        (have values -1) because that's the smallest distance to a nearby zero they can have.
        Then, we add those newly assigned elements to the queue to keep track of them and apply the same process above with their adjacent cells.
        - Time complexity: O(N).
        - Space complexity: O(N)
        """
        row = len(mat)
        col = len(mat[0])
        assigned_value_cells = deque()
        ans = [[-1 for _ in range(col)] for __ in range(row)]

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    assigned_value_cells.append((i, j))

        while len(assigned_value_cells) > 0:
            i, j = assigned_value_cells.popleft()
            curr_distance = ans[i][j]
            # top
            if i - 1 >= 0 and ans[i-1][j] == -1:
                calculate_nearest_zero_distance(
                    ans, i-1, j, curr_distance, assigned_value_cells)
            # right
            if j + 1 < col and ans[i][j+1] == -1:
                calculate_nearest_zero_distance(
                    ans, i, j+1, curr_distance, assigned_value_cells)
            # bottom
            if i + 1 < row and ans[i+1][j] == -1:
                calculate_nearest_zero_distance(
                    ans, i+1, j, curr_distance, assigned_value_cells)
            # left
            if j - 1 >= 0 and ans[i][j-1] == -1:
                calculate_nearest_zero_distance(
                    ans, i, j-1, curr_distance, assigned_value_cells)

        return ans
