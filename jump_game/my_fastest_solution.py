# https://leetcode.com/problems/jump-game/description/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        - Set the last element in the array as your initial target.
        - Traverse the array from the end to the first element in the array.
        - If the current index is reachable from any preceding index, based on the value at that index, make
        that index the new target.
        - If you reach the first index of the array without finding any index from which the current target
        is reachable, return False
        - Else, if you are able to move each current target backward all the way to the first 
        index of the array, you've found a path from the start to the end of the array. return True.

        """
        target = len(nums) - 1
        i = len(nums) - 2

        while i >= 0:
            if nums[i] + i >= target:
                target = i

            i -= 1

        return target <= 0
