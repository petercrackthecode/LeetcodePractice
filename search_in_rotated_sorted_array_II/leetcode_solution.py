# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid: int = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[left]:
                left += 1
            elif nums[mid] > nums[left]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
