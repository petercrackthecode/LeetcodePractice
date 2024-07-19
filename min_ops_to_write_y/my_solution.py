# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/
from typing import List, Set, Dict

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        '''
        - all values at cells belong to Y are equal.
        - all values at cells not belonging to Y are equal
        - The values at cells belonging to the Y are different from the values at cells not belonging to Y

        - return min num of changes (from any value -> 0/1/2) to write letter Y
        [     0  1  2
        0    [1, 2, 2],
        1    [1, 1, 0],
        2    [0, 1, 0]
        ]

        Y_line = {
            0: 0,
            1: 3,
            2: 1
        }

        outside_Y = {
            0: 3,
            1: 1,
            2: 1
        }

        [
        0    [1, 0, 1],
        1    [0, 1, 0],
        2    [0, 1, 0]
        ]

        [    0  1  2  3  4
            [0, 1, 0, 1, 0],  0
            [2, 1, 0, 1, 2],  1
            [2, 2, 2, 0, 1],  2
            [2, 2, 2, 2, 2],  3
            [2, 1, 2, 2, 2]   4
        ]

        0: 2 + 3 = 5

        outside_Y = {
            0: 3,
            1: 4,
            2: 11
        }
        3 + 11 = 14
        total = 5 + 14
        - find the most frequent value (0, 1, 2) in the outside_Y
        Y_line  outside_Y
        0        1
        0        2
        1        2
        1        0
        2        1
        2        0

        4 + 3 = 7 + (2 + 3) = 12
        3 <= n <= 49
        
        mid = n // 2
        make a choice of picking (0, 1, 2) for the Y_line: pick 0
        count:int = 0
        iterate thru the entire array:
        - at cell (r, c):
            - if (r, c) is within the Y_line:
                - if grid[r][c] != 0:
                    - increment the current count by 1
                - if (r, c) is within the outside_Y:
                    - grid[r][c] == 1:
                        case_0_1 += 1

        [     0  1  2
        0    [1, 2, 2],
        1    [1, 1, 0],
        2    [0, 1, 0]
        ]

        Y_line = {
            0: 0,
            1: 3,
            2: 1
        }

        outside_Y = {
            0: 3,
            1: 1,
            2: 1
        }
        '''
        def cost_to_switch(num_freq: Dict[int, int], chosen_key:int):
            return sum([val for (key, val) in num_freq.items() if key != chosen_key])

        n:int = len(grid)
        mid:int = n // 2
        Y_line:Dict[int, int] = {0: 0, 1: 0, 2: 0}
        outside_Y:Dict[int, int] = {0: 0, 1: 0, 2: 0}

        for row in range(n):
            for col in range(n):
                '''
                [     0  1  2
                0    [1, 2, 2],
                1    [1, 1, 0],
                2    [0, 1, 0]
                ] | n = 3 | mid = 1
                '''
                # check if the position lies on the top left side of the Y line
                if row == col and row <= mid: # top left side of Y
                    curr_val:int = grid[row][col]
                    Y_line[curr_val] += 1
                elif row + col == n - 1 and row < mid: # top right side of Y
                    curr_val:int = grid[row][col]
                    Y_line[curr_val] += 1
                elif col == mid and row > mid: # middle line to bottom of Y
                    curr_val:int = grid[row][col]
                    Y_line[curr_val] += 1
                else:
                    curr_val:int = grid[row][col]
                    outside_Y[curr_val] += 1

        min_ops:int = n*n + 1
        
        for picked_Y_val in Y_line.keys():
            cost_to_switch_in_Y:int = cost_to_switch(Y_line, picked_Y_val)
            # we cannot choose pick_Y_val below => we can only choose the number in other_keys
            selectable_non_y_vals:Set[int] = {0, 1, 2} - {picked_Y_val}

            for picked_non_y_val in selectable_non_y_vals:
                # flip all the outside of the Y line value to outside_key
                # pick other key as the value to flip to at cells outside of Y_lines
                # calculate the cost to flip the outside to other_key
                cost_to_switch_outside_Y:int = cost_to_switch(outside_Y, picked_non_y_val)
                curr_cost:int = cost_to_switch_in_Y + cost_to_switch_outside_Y
                min_ops = min(min_ops, curr_cost)

        return min_ops




            


            




