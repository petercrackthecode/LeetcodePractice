# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast = slow:
                break
        
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast
