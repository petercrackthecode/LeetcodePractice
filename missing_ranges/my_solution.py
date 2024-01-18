# https://leetcode.com/problems/missing-ranges/
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        """
        ans = []
        iterate through nums:
            for (i, num) in enumerate(nums):
                if i == 0:
                    if num > lower:
                        ans.append([lower, num])
                elif num - 1 > nums[i-1]:
                    ans.append(nums[i-1] + 1, num - 1)
            if nums[-1] < upper:
                ans.append(nums[-1] + 1, upper)
            return ans
        """
        if len(nums) == 0:
            return [[lower, upper]]

        ans = []
        for (i, num) in enumerate(nums):
            if i == 0:
                if num > lower:
                    ans.append([lower, num-1])
            elif num - 1 > nums[i-1]:
                ans.append([nums[i-1] + 1, num - 1])

        if nums[-1] < upper:
            ans.append([nums[-1] + 1, upper])

        return ans
