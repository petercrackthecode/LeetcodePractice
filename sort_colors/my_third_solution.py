# https://leetcode.com/problems/sort-colors/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Put all the blues to the back: have one pointers called blue (initialized to a position where nums[blue] == 2) and one is non_blue (initialized to an index where nums[non_blue] !== 2). 
        keep incrementing blue while nums[blue] != 2
        keep decrementing non_blue while nums[non_blue] == 2
        swap the numbers at blue and non_blue altogether.
        repeat the steps above while blue < non_blue

        have two pointers: red (0) & white (len(nums) - 1)
        keep incrementing red while nums[red] != 1
        keep decrementing white while nums[white] != 0
        swap the numbers at indices red & white.
        repeat the steps above while blue red < white
        """
        [blue, non_blue] = [0, len(nums) - 1]
        while blue < non_blue:
            if nums[blue] != 2:
                blue += 1
            elif nums[non_blue] == 2:
                non_blue -= 1
            else:
                [nums[blue], nums[non_blue]] = [nums[non_blue], nums[blue]]

        [red, white] = [0, len(nums) - 1]
        while red < white:
            if nums[red] != 1:
                red += 1
            elif nums[white] != 0:
                white -= 1
            else:
                nums[red], nums[white] = nums[white], nums[red]
