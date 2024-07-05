# https://leetcode.com/problems/binary-search/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid:int = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # move right
                left = mid + 1
            else: # move left
                right = mid - 1
        
        return -1