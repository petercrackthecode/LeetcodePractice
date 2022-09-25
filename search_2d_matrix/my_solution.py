# https://leetcode.com/problems/search-a-2d-matrix/
def has_target(one_dimension_array: List[int], target: int) -> bool:
    start = 0
    end = len(one_dimension_array) - 1
    while start <= end:
        mid = (end - start)//2 + start
        if one_dimension_array[mid] == target:
            return True
        elif one_dimension_array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


def find_row_that_may_contain_number(matrix: List[List[int]], target: int) -> int:
    """
    row = len(matrix)
    column = len(matrix[0])
    Find the i index where:
    matrix[i][0] <= target <= matrix[i][column - 1]
    elif target < matrix[i][0]:
        end = i-1
    else: # matrix[i][column-1] < target
        start = i+1
    """
    ROW = len(matrix)
    COL = len(matrix[0])
    start = 0
    end = ROW - 1
    while start <= end:
        mid = (end - start)//2 + start
        if matrix[mid][0] <= target <= matrix[mid][COL - 1]:
            return mid
        elif target < matrix[mid][0]:
            end = mid - 1
        else:  # matrix[mid][COL-1] < target
            start = mid + 1
    return -1


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        + First, find the row that the target number can belong to: have a helper function called find_row_that_may_contain_number(matrix: List[List[int]], target: int) -> int. Call the result of the above function possible_row.
        + If possible_row >= 0:
            1d_array = matrix[possible_row]
            return has_target(1d_array: List[int], target: int) -> bool
        + Otherwise: return False
        """
        possible_row = find_row_that_may_contain_number(matrix, target)
        if possible_row >= 0:
            one_dimension_array = matrix[possible_row]
            return has_target(one_dimension_array, target)
        else:
            return False
