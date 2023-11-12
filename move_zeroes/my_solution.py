# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        p = 0

        while z < len(nums) and p < len(nums):
            if nums[z] != 0:
                z += 1
                continue
            if nums[p] == 0:
                p += 1
                continue

            # arr[z] == 0 and arr[p] != 0
            if z < p:
                [nums[z], nums[p]] = [nums[p], nums[z]]
            else:  # z >= p
                p += 1
