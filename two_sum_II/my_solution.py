from typing import List


def binary_search_except_index(numbers: List[int], to_be_found_number: int, omitted_index: int):
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (end - start) // 2 + start
        if numbers[mid] == to_be_found_number and mid != omitted_index:
            return mid
        elif numbers[mid] >= to_be_found_number:
            end = mid - 1
        else:
            start = mid + 1
    return -1


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        sorted non-decreasing list => binary search.
        iterate through the list, pick element i (starting from 0). Assign to be found number as:
        to_be_found_number = target - numbers[i]
        Have a binary search helper function called binary_search_except_index(numbers, target=to_be_found_number, omitted_index=i)
        if binary_search_except_index returns an index j >= 0:
        return [i+1, j+1]
        otherwise, continue the loop
        """
        for i, num in enumerate(numbers):
            to_be_found_number = target - num
            found_index = binary_search_except_index(
                numbers, to_be_found_number, i)
            if found_index >= 0:
                return sorted([i+1, found_index+1])

        return [0, 1]
