# https://leetcode.com/problems/01-matrix/
from typing import List


class Solution:
    def __init__(self):
        self.distance_matrix = list()
        # is_visited: check if the element is already visited, so not to recursively call it again.
        # key: a pair of tuple
        # value: bool
        self.is_visited = dict()

    def getCellDistanceToNearestZero(self, mat: List[List[int]], r: int, c: int) -> int:
        # Only update the self.distance_matrix at the [r][c] position if it hasn't been updated yet.
        print('row = ', r, ', column = ', c)
        print("mat = ", mat)
        if self.distance_matrix[r][c] == -1:
            columns, rows = len(mat[0]), len(mat)
            LARGEST_POSSIBLE_DISTANCE = rows * columns - 1
            if mat[r][c] == 0:
                self.distance_matrix[r][c] = 0
            else:
                print("called")
                top_matrix_distance = self.getCellDistanceToNearestZero(
                    mat, r-1, c) if (r-1 >= 0 and not (r, c) in self.is_visited) else LARGEST_POSSIBLE_DISTANCE
                bottom_matrix_distance = self.getCellDistanceToNearestZero(
                    mat, r+1, c) if (r+1 < rows and not (r, c) in self.is_visited) else LARGEST_POSSIBLE_DISTANCE
                left_matrix_distance = self.getCellDistanceToNearestZero(
                    mat,  r, c-1) if (c-1 >= 0 and not (r, c) in self.is_visited) else LARGEST_POSSIBLE_DISTANCE
                right_matrix_distance = self.getCellDistanceToNearestZero(
                    mat, r, c+1) if (c+1 < columns and not (r, c) in self.is_visited) else LARGEST_POSSIBLE_DISTANCE

                self.distance_matrix[r][c] = 1 + min(bottom_matrix_distance,
                                                     right_matrix_distance)
        else:
            print("self.distance_matrix is already updated")

        self.is_visited[(r, c)] = True
        return self.distance_matrix[r][c]

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.distance_matrix = [[-1] * len(mat[0])] * len(mat)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                self.getCellDistanceToNearestZero(
                    mat, r, c)

        print("The original matrix = ", mat)

        return self.distance_matrix


updated_matrix = Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
print("updated_matrix = ", updated_matrix)
