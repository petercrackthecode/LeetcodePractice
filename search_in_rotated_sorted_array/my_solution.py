# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


def get_rotation_index(nums: List[int]) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (end - start) // 2 + start

        left_bound = float('+inf') if mid == 0 else nums[mid-1]
        right_bound = float('+inf') if mid == len(nums)-1 else nums[mid+1]
        if left_bound > nums[mid] and nums[mid] < right_bound:
            return mid
        elif nums[0] <= nums[mid]:
            start = mid + 1
        elif nums[mid] <= nums[len(nums)-1]:
            end = mid - 1
    # rotating a list at position 0 will return the same original list
    return 0


def binary_search(nums: List[int], target: int, left: int, right: int) -> int:
    start = left
    end = right
    while start <= end:
        mid = (end - start) // 2 + start
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotation_index = get_rotation_index(nums)
        if rotation_index > 0:
            possible_index_if_found_on_left = binary_search(
                nums, target, 0, rotation_index-1)
            if possible_index_if_found_on_left > -1:
                return possible_index_if_found_on_left

        if rotation_index < len(nums):
            possible_index_if_found_on_right = binary_search(
                nums, target, rotation_index, len(nums) - 1)
            if possible_index_if_found_on_right > -1:
                return possible_index_if_found_on_right

        return -1
