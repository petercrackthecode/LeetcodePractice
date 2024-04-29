# https://leetcode.com/problems/01-matrix/
from typing import List, Tuple, Deque, Set
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        - spreaders:Deque[Tuple[int, int]] = deque()
        - have a set of tuples to save all checked nodes: visited:Set[Tuple[int, int]] = set()
        - loop thru the list, save all the coordinates of the zero elements to a queue called spreaders
        - loop while spreaders is not empty:
            - pop an element from the beginning of spreaders: (row, col) = spreaders.popleft()
            - get the current value: curr_val = mat[row][col]
            - add the said coordinate to our set of visited coordinates: visited.add((row, col))
            - check 4 positions: top (row-1, col), bottom (row+1, col), left (row, col-1), right (row, col+1):
                - does the coordinates exist within our bounds: if yes, move to the next step.
                - does the coordinates exist within visited: if no, move to the next step.
                - is mat[this_row][this_col] different from 0: if yes, move to the next step
                - assign: mat[this_row][this_col] = curr_val + 1
                - add (this_row, this_col) to visited.
                - append the tuple (this_row, this_col) to the back of spreaders
        """
        spreaders: Deque[Tuple[int, int]] = deque()
        visited: Set[Tuple[int, int]] = set()

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    spreaders.append((row, col))

        def is_valid_coord(row: int, col: int) -> bool:
            nonlocal mat
            MAX_ROW, MAX_COL = len(mat), len(mat[0])

            return 0 <= row < MAX_ROW and 0 <= col < MAX_COL

        def populate_nearby_coords(row: int, col: int, curr_val: int) -> None:
            nonlocal spreaders, visited

            for r, c in (
                (row - 1, col),  # top
                (row + 1, col),  # bottom
                (row, col - 1),  # left
                (row, col + 1),  # right
            ):
                if not is_valid_coord(r, c) or (r, c) in visited or mat[r][c] == 0:
                    continue

                mat[r][c] = curr_val + 1
                visited.add((r, c))
                spreaders.append((r, c))

        while bool(spreaders):
            (row, col) = spreaders.popleft()
            curr_val = mat[row][col]
            visited.add((row, col))
            populate_nearby_coords(row, col, curr_val)

        return mat
