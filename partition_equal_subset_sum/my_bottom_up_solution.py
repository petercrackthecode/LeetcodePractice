# https://leetcode.com/problems/partition-equal-subset-sum/
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        - get the total sum of every elements in nums.
        - get the half total sum: half_sum:float = sum(nums) / 2
        - if half_sum is not an integer (half_sum != int(half_sum)): return False immediately.
        - otherwise, convert the problem back to can_get_sum_in_nums(half_sum) -> bool.

        """

        # nums = [1,5,11,5]
        half_sum: float = sum(nums) / 2
        if half_sum != int(half_sum):
            return False

        target: int = int(half_sum)
        nums.sort()

        """
        -1: uninitialized.
         0: False
         1: True
        """
        # row: curr_target range from 0..target -> target + 1 rows
        # column: the number of elements included within the array 0..len(nums) -> len(nums) + 1 columns
        dp: List[List[int]] = [
            [False for _ in range(len(nums) + 1)] for __ in range(target + 1)
        ]

        # Initialize all the columns on the first row (where the curr_target is 0) to True
        for col in range(len(nums) + 1):
            dp[0][col] = True
        # Initialize all the rows since the second row at column 0 (where there's no elements included) to False
        for row in range(1, target + 1):
            dp[row][0] = False

        for curr_target in range(1, target + 1):  # row
            for item in range(1, len(nums) + 1):  # col
                num = nums[item - 1]
                if (
                    num > curr_target
                ):  # we cannot use the current item to form the curr_target => ignore it & use the result from the previous column
                    dp[curr_target][item] = dp[curr_target][item - 1]
                else:  # num <= curr_target => can fill the item
                    dp[curr_target][item] = (
                        dp[curr_target][item - 1] or dp[curr_target - num][item - 1]
                    )

        return dp[target][len(nums)]
