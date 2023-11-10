# https://leetcode.com/problems/jump-game/description/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
         0 1 2 3 4
        [2,3,1,1,4]

        - Start from the beginning (0), collect all the nearby indexes that we can jump into.
        - Among all those indexes, jump to the index k with the biggest reach (max(nums[j] + i))
        - i = k
        - keep doing so until i >= len(nums) - 1 (last_index) or nums[i] == 0
        - return i >= len(nums) - 1
        """
        i = 0

        while not (i >= len(nums) - 1 or nums[i] == 0):
            steps = nums[i]
            if steps + i >= len(nums) - 1:
                return True

            index_with_biggest_reach = i + 1
            for st in range(1, steps + 1):
                j = i + st
                if nums[j] + j > nums[index_with_biggest_reach] + index_with_biggest_reach:
                    index_with_biggest_reach = j
            i = index_with_biggest_reach

        return i >= len(nums) - 1
