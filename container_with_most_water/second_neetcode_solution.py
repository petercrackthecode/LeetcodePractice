# https://leetcode.com/problems/trapping-rain-water/
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        # OBSERVATION
        - we cannot trap the water by the borders.
        - if the length of height is less than 3, we cannot hold any water => return 0
        
                  0  1  2  3  4  5  6  7  8  9 10 11
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
                     l
                           r

        temp_water += height[l] - height[r]

        height = [4, 2, 0, 3, 2, 5]
                  *
        * # # # # *
        * # # * # *
        * * # * * *
        * * # * * *


        output = 5          
        *         
        *     *   *
        * *   * * *
        * *   * * *
          l
              r

          * * *
          * * *

        we have 2 edges: left and right.
        - for a left edge to trap water, it has to be longer than all edges on its left.
        - for a right edge to trap water, it has to be longer than all edges on its right.

        left = mid - 1
        right = mid + 1

        5


                  0  1  2  3  4  5  6  7  8  9 10 11
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

         0 1 2 3 4 5 6 7 8 9 10 11
        |              *        |
        |      *       * *   *  |
        |  *   * *   * * * * * *|
           l
                             r

        curr_lower_edge = 1
        width = 11 - 1 - 1 = 9
        total = 1 x 9 = 9

        how to we decide when we should move one edge (left) or another (right)?


        use the shorter edge as the pointer       

        for an edge l, keep moving the edge r until height[l] <= height[r]

        for 2 edges l and r to hold some water in between, there should be an element i where l < i < r and height[i] < height[l] and height[i] < height[r]

        for an of height[l], the amount of water we can currently hold will depends on the edge height[r] that is greater than or equal to height[l]


        ** Solution 1:
        - Say max_height_left is the greater height on the left of an index i (not including height[i])
        - Say max_height_right is the greater height on the right side of an index i (not including height[i])
        - Say min_edge is the shortest edge between max_height_left and max_height_right for i
        - At any index i, the amount of water we can trap at column i is the max(0, min_edge - height[i]) (since we cannot trap negative amount of water at any column)
        - if we do this step for all i from 0 -> len(height) - 1, we have the total amount of water we can trap.
        - Since the step of calculating max_height_left and max_height_right can be expensive (O(N^2) in total), we use a table max_left:List[int] (n elements) and max_right:List[int] (n elements) to keep track of the max_left and max_right at any given index i.
        - loop from left -> right to populate max_left
        - loop from right -> left to populate max_right

        ** Solution 2:
        - we still use the same formula: the amount of water can be contained at an index i is the max(0, min(max_height_from_left_of_i, max_height_from_right_of_i) - height[i]))
        - have 2 pointers left and right. left = 0 and right = len(height) - 1
        - have 2 value max_left represents the greatest height on the left side of the left ptr, while max_right represents the greatest height on the right side of the right ptr.
        - loop: while left <= right:
            - if max_left is smaller than or equal to max_right => that's the shorter edge between max_height on the left side of the left ptr, and max_height on the right side of the right ptr (since max_left is smaller than a value on the left side of the left ptr, we don't need to know the actual maximum value on the right side of the left ptr to decide the min between 2 edges) => we calculate the amount of water we can hold at the index left by the formula: water_amount:int = max(0, max_left - height[i]).
            - we then move the left ptr forward.
            - we do the similar step if max_right is greater than max_left.
        - The reason we calculate the condition (left <= right) instead of (left < right) because when a ptr left or right move to a new index (left += 1 or right -= 1), we don't evaluate the amount of water we can hold at that index yet. That's why we gotta let them cross so one of 'em will calculate the amount of water at the index where left == right.
        '''
        max_left:int = 0
        max_right:int = 0

        ans:int = 0

        left:int = 0
        right:int = len(height) - 1

        while left <= right:
            if max_left <= max_right:
                # move the left ptr
                trapped_water:int = max(0, max_left - height[left])
                ans += trapped_water
                max_left = max(max_left, height[left])
                left += 1
            else: # max_left > max_right => move the right ptr
                trapped_water:int = max(0, max_right - height[right])
                ans += trapped_water
                max_right = max(max_right, height[right])
                right -= 1

        return ans