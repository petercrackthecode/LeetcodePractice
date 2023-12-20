# https://leetcode.com/problems/sort-colors/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        declare three pointers: red (initialized to the array's starting index), white (initialized to the array's starting index), and blue (initialized to the array's last index).
        if colors[white] is 0, we swap the values of colors[white] and colors[red]. We also increment both the white and red pointers by 1.
        otherwise, if colors[white] is 1, the number is already at the correct position, so no swapping is performed, and we just increment the white pointer by 1.
        Otherwise, colors[white] will be 2, so we swap the values colors[white] and colors[blue], then decrement the blue pointer by 1.
        Repeat the above step while red <= white <= blue
        """
        [red, white, blue] = [0, 0, len(nums) - 1]

        while red <= white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] == 1:  # at the correct position
                white += 1
            else:  # nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
