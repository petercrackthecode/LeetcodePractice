# https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        add two adjacent elements and replace them with their sum
        return min num of operations to turn the array into a palindrome

        [4,3,2,1,2,3,1]
        [4,3,2,1,2,4]
        [3,2,1,2]
        [3,2,3]
        [2]

        [1,2,3,4]
        - if I add two number next to each other & get a new number at i, I'll get a new list. afterward, is the num at the len(new_list) - i - 1 position equals to new_list[i]

        final list: [abc d cba]
                    / \
                   e + f
        if we cannot find the equal pair in the border after any operation, what do we do?

        [1, 3, 3, 5, 1, 1]
        [1,  6  ,  6  , 1]
            [6  , 5, 1]
        ans = 2

        do we pick the pair whose sum is smaller when we have two sums but no equal pair?
         l. r
        [0, 0]
        """
        ops = 0

        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
                continue
            # nums[left] != nums[right]
            # [1, 3, 4]
            ops += 1
            # no chance of equal sum yet
            # [1,2,3,4]
            # nums[left] != nums[right]
            two_sum_left = nums[left] + nums[left+1]
            two_sum_right = nums[right] + nums[right-1]
            if two_sum_left <= two_sum_right:
                nums[left+1] = two_sum_left
                left += 1
            else:  # two_sum_left > two_sum_right
                nums[right-1] = two_sum_right
                right -= 1

        return ops
