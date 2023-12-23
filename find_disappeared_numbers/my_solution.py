# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()

        unique_nums = set()

        for num in range(1, len(nums) + 1):
            unique_nums.add(num)

        for num in nums:
            unique_nums.discard(num)

        return list(unique_nums)
