# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        have a set called unique_nums 
        save all the unique numbers within the range [0, n] to unique_nums
        loop: for each number in nums, remove that number from unique_nums
        convert unique_nums to a list, and return the first element of the list: list(unique_nums)[0]
        """
        unique_nums = set()
        for num in range(len(nums)+1):
            unique_nums.add(num)

        for num in nums:
            unique_nums.discard(num)

        return list(unique_nums)[0]
