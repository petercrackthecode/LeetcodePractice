# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List, Set


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        - ans = 0
        - have a set called unchecked_nums to save all the unchecked numbers from the list. initialize unchecked_nums = set(nums)
        - iterate thru each number in nums:
            - if the number doesn't exist in unchecked_num (the number is already checked), skip to the next number (continue)
            - set the curr_range = 1
            - set left = num - 1
            - set right = num + 1
            - loop while left exists in unchecked_nums:
                - discard left from unchecked_nums
                - increment curr_range by 1.
                - decrement left by 1.
            - loop while right exists in unchecked_nums:
                - discard right from unchecked_nums
                - increment curr_range by 1.
                - increment right by 1
            - assign: ans = max(ans, curr_range)

        - return ans
        """
        ans: int = 0

        unchecked_nums: Set[int] = set(nums)

        for num in nums:
            if num not in unchecked_nums:
                continue

            unchecked_nums.discard(num)

            left: int = num - 1
            right: int = num + 1
            curr_range: int = 1

            while left in unchecked_nums:
                unchecked_nums.discard(left)
                curr_range += 1
                left -= 1

            while right in unchecked_nums:
                unchecked_nums.discard(right)
                curr_range += 1
                right += 1

            ans = max(ans, curr_range)

        return ans
