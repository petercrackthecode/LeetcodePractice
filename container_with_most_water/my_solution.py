# https://leetcode.com/problems/container-with-most-water/
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
                  0  1  2  3  4  5  6  7  8
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        output = 49
        (i, 0) and (i, height[i])

        only change is the 7-axis

        i = 0
            (0, 0) and (0, 1)
        i = 1
            (1, 0) and (1, 8)

        return max amount of water from a container

        i = 0

        2 pointers

        l = 0
        r = len(heights) - 1

        area_of_water = min(heights[l], heights[r]) * (r - l)
        
                  l ->
                                     <-   r
                  0  1  2  3  4  5  6  7  8
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

        area = 1 * 7 = 7 (0, 8)

        area = 7 * 7 = 49 (1, 8)
        
        area = 1 * 7 = 7 (0, 7)

        the area of water depends heavily on the height of the lower line.
        as we move the pointers, the width (l-r) will decrease.

        Our goal is to increase the height of the shorter line.

        - each time, we keep track of the area of water and compare it with our global max_area
        - if we have two lines (heights[l] and heights[r]) at the same height:
            - we can move either l forward or r backward: move the left pointer forward.
        - otherwise, if heights[l] > heights[r]:
            - move the right pointer backward.
        - otherwise (heights[l] < heights[r]):
            - move the left pointer forward.
        '''
        left:int = 0
        right:int = len(height)-1
        max_area:int = 0

        while left < right:
            container_height:int = min(height[left], height[right])
            container_width:int = right - left
            curr_area:int = container_height * container_width
            max_area = max(max_area, curr_area)

            # move the pointers
            if height[left] >= height[right]:
                # move the right ptr backward
                right -= 1
            else: # height[left] < height[right]
                left += 1

        return max_area