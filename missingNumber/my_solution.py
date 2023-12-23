# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        [0, 1, 3]
        n distinct numbers in the range [0, n]
        sort the nums array.
        have a variable called counter to track the next missing number. counter = 0
        for each index i [0..len(nums) - 1] in nums, if nums[i] is greater than counter: break the loop.
        otherwise, increment counter by 1

        return counter.
        """
        nums.sort()
        counter = 0
        for num in nums:
            if num > counter:
                break
            counter += 1

        return counter
