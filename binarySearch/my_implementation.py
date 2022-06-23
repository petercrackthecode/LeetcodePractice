from typing import List


def binary_search(target: int, nums: List[int]) -> bool:
    left_index: int = 0
    right_index: int = len(nums) - 1
    mid_index: int = -1

    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        if target == nums[mid_index]:
            return True
        elif target > nums[mid_index]:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    # No number found
    return False


print("True" if binary_search(3, [1, 1, 1, 1, 1, 1]) else "False")
