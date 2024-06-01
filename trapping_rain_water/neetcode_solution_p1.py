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
        '''
        max_left:List[int] = []
        max_right:List[int] = []

        curr_max_left:int = 0

        for i in range(len(height)):
            max_left.append(curr_max_left)
            curr_max_left = max(curr_max_left, height[i])

        curr_max_right:int = 0

        for i in reversed(range(len(height))):
            max_right.append(curr_max_right)
            curr_max_right = max(curr_max_right, height[i])
        
        max_right = max_right[::-1]

        ans:int = 0

        for i in range(len(height)):
            min_edge:int = min(max_left[i], max_right[i])
            ans += max(0, min_edge - height[i])

        return ans