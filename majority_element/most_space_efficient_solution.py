# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, count = nums[0], 1

        for i in range(1, len(nums)):
            if nums[i] != majority:
                count -= 1
            elif nums[i] == majority:
                count += 1

            majority = nums[i] if count < 0 else majority
            count = 1 if count < 0 else count

        return majority
