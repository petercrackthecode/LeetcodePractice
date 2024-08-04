# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # since nums's length is within the range [0, 5000], we can do a linear search here.
        def find_pivot_idx(nums) -> int:
            for i in range(1, len(nums)):
                prev_num: int = nums[i - 1]
                curr_num: int = nums[i]

                if prev_num > curr_num:
                    return i

            return 0

        def binary_search_in_range(left: int, right: int, target: int) -> bool:
            nonlocal nums

            while left <= right:
                mid: int = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:  # move right
                    left = mid + 1
                else:  # move left
                    right = mid - 1

            return False

        pivot_idx: int = find_pivot_idx(nums)
        return binary_search_in_range(
            0, pivot_idx - 1, target
        ) or binary_search_in_range(pivot_idx, len(nums) - 1, target)
