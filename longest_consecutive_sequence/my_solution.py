# https://leetcode.com/problems/longest-consecutive-sequence/description/
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [0,3,7,2,5,8,4,6,0,1]
        [0, 0, 1, 2, 3, 4, 5, 6, 7, 8]

        - we need to have a set to check if a number exists in our list
        - we need to have a dictionary to see if the number is already check.

        check if the number is already checked

        we need a data structure: a group of sets.
        """
        if len(nums) == 0:
            return 0

        ans: int = 1
        nums.sort()
        curr_streak: int = 1

        for i in range(1, len(nums)):
            curr_num, prev_num = nums[i], nums[i - 1]
            if curr_num - prev_num > 1:
                curr_streak = 1
            elif curr_num == prev_num:  # curr_num - prev_num == 0
                continue
            else:  # curr_num - prev_num == 1
                curr_streak += 1

            ans = max(ans, curr_streak)

        return ans
