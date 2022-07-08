# https://leetcode.com/problems/01-matrix/
from typing import List


class Solution:
    def __init__(self):
        self.distance_matrix = list()

    def getCellDistanceToNearestZero(self, mat: List[List[int]], r: int, c: int) -> int:
        # Only update the self.distance_matrix at the [r][c] position if it hasn't been updated yet.
        print('row = ', r, ', column = ', c)
        if self.distance_matrix[r][c] == -1:
            columns, rows = len(mat[0]), len(mat)
            if mat[r][c] == 0:
                self.distance_matrix[r][c] = 0
            else:
                top_matrix_distance = self.getCellDistanceToNearestZero(
                    mat, r-1, c) if r-1 >= 0 else float('inf')
                bottom_matrix_distance = self.getCellDistanceToNearestZero(
                    mat, r+1, c) if r+1 < rows else float('inf')
                left_matrix_distance = self.getCellDistanceToNearestZero(
                    mat,  r, c-1) if c-1 >= 0 else float('inf')
                right_matrix_distance = self.getCellDistanceToNearestZero(
                    mat, r, c+1) if c+1 < columns else float('inf')

                print(
                    f"top_matrix_distance = {top_matrix_distance}, \
                      bottom_matrix_distance = {bottom_matrix_distance}, \
                        left_matrix_distance = {left_matrix_distance}, \
                          right_matrix_distance = {right_matrix_distance}")

                self.distance_matrix[r][c] = 1 + min(top_matrix_distance, bottom_matrix_distance,
                                                     left_matrix_distance, right_matrix_distance)
        else:
            print("self.distance_matrix is already updated")
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
