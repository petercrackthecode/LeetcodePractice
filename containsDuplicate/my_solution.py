# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()

        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)

        return False
