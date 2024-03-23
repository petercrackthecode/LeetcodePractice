# https://leetcode.com/problems/move-zeroes/
from collections import deque
from typing import Deque, List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        - have a deque() called non_zeroes nums to save all the non zero numbers
        - iterate thru nums: for each num in nums:
            - if num is different from 0:
                - append num to non_zeroes
        - loop: for each index i in range(len(nums)):
            - if non_zeroes is not empty:
                - popped an element from the front of non_zeroes
                - assign nums[i] = the popped_element.
            - otherwise, assign nums[i] = 0
        """
        non_zeroes: Deque[int] = deque()

        for num in nums:
            if num != 0:
                non_zeroes.append(num)

        for i in range(len(nums)):
            if len(non_zeroes) > 0:
                nums[i] = non_zeroes.popleft()
            else:
                nums[i] = 0
