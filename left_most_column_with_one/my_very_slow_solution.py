# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        get the row and the column of the matrix.
        have a variable called ans initialized to column + 1 (an invalid value)

        loop through for each r from 0 to row-1 (inclusively): apply custom binary search to the row r to find the leftmost column with a 1 in it in the current row.
            then, get the minimum between the current_leftmost and ans, and assign it to ans.

        return ans if ans is smaller than column, otherwise return -1
        """
        [row, col] = binaryMatrix.dimensions()
        ans = col + 1

        def leftmost_col_with_one(curr_row: int) -> int:
            nonlocal binaryMatrix, col
            [left, right] = [0, col-1]
            found = -1

            while left <= right:
                mid = left + (right - left) // 2
                if binaryMatrix.get(curr_row, mid) == 1:
                    found = mid if found == -1 else min(found, mid)
                    right = mid - 1
                else:  # binaryMatrix.get(curr_row, mid) == 0 => move right
                    left = mid + 1

            return found

        for r in range(row):
            curr_leftmost_with_one = leftmost_col_with_one(r)
            if curr_leftmost_with_one > -1:
                ans = min(ans, curr_leftmost_with_one)

        return ans if ans < col else -1
