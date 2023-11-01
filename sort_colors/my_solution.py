# https://leetcode.com/problems/sort-colors/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        we have nums. in nums, there are 3 values: 0, 1, 2

        two pointers approach: left = 0, right = len(nums) - 1

        - run through the array for the first time, move all the 2s to the end of nums by swapping.
        - get the last index within nums that is not 2 (all the 2s are at the right of nums after the last operation). right = last_not_blue_index
        - 
            [left, right] = [0, len(nums) - 1]

            while left < right:
                while nums[left] != 2 and left < right:
                    left += 1
                while nums[right] == 2 and right > left:
                    right -= 1
                arr[left], arr[right] = arr[right], arr[left]

            last_not_blue_index = len(nums) - 1
            while last_not_blue_index >= 0 and nums[last_not_blue_index] == 2:
                last_not_blue_index -= 1

            [left, right] = [0, last_not_blue_index]

            while left < right:
                while nums[left] != 1 and left < right:
                    left += 1
                while nums[right] == 1 and right > left:
                    right -= 1
                arr[left], arr[right] = arr[right], arr[left]
        """
        [left, right] = [0, len(nums) - 1]

        while left < right:
            while nums[left] != 2 and left < right:
                left += 1
            while nums[right] == 2 and right > left:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]

        last_not_blue_index = len(nums) - 1
        while last_not_blue_index >= 0 and nums[last_not_blue_index] == 2:
            last_not_blue_index -= 1

        [left, right] = [0, last_not_blue_index]

        while left < right:
            while nums[left] != 1 and left < right:
                left += 1
            while nums[right] == 1 and right > left:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
