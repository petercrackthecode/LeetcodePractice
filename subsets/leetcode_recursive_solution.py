# https://leetcode.com/problems/subsets/
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start:int, path: List[int]):
            result.append(path)
            for i in range(start, len(nums)):
                backtrack(i+1, path + [nums[i]])


        result:List[List[int]] = []

        backtrack(0, [])

        return result