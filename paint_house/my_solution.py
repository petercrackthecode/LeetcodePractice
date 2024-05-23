# https://leetcode.com/problems/paint-house/
from typing import Set, List, DefaultDict, Tuple
from collections import defaultdict

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        '''
        0    1      2
        red, blue, green

        costs = [
              0  1  2
0            [17,2,17],
1            [16,16,5],
2            [14,3,19]
        ]
                    
0                     0
            /(17, 0)      |(2,1)            \(17, 2)
1           17               2                  17
        /(16,0) \(5,2)  /(16,0) \(5,2)      /(16,0) \(16, 1)
2      33     22   18      7       33     33
  /(3,1) \(19,2)

    - loop: for row r from 0 -> len(costs)-1
    - repeating subproblem: given a color (column) c for a house at row r, what's the minimum cost we can get from painting that house c and now on?
        - loop: for curr_color in range(2)
            - next_house_colors:List[int] = [next_color for next_color in (0, 1, 2) if next_color != curr_color]
            - next_house_paint_cost_1 = get_paint_cost(r+1, next_house_colors[0])
            - next_house_paint_cost_2 = get_paint_cost(r+1, next_house_colors[1])
            - min_cost_from_house[r] = costs[r][curr_color] + min(next_house_paint_cost_1, next_house_paint_cost_2)
    
    - return get_paint_cost(-1, -1)
        '''
        #                       Tuple[house, color] -> cost: given a house idx and its painted color, return the min_cost to paint from that house
        n:int = len(costs)
        # key: from_house: the index of the house we start painting from
        # value: avail_colors: the set of available colors we can paint the current house
        min_cost_from_house:DefaultDict[Tuple[int, int], int] = defaultdict(lambda: 20 * n + 1)

        #                                        (0, 1, 2)
        def get_min_paint_cost(from_house: int, last_color: int) -> int:
            '''
            [     0  1  2
            0    [17,2,17],
            1    [16,16,5],
            2    [14,3,19]
            ]
            '''
            nonlocal min_cost_from_house, n

            if from_house >= n:
                return 0

            if (from_house, last_color) in min_cost_from_house:
                return min_cost_from_house[(from_house, last_color)]

            min_paint_cost_curr:int = 20 * n + 1 # dummy value- n houses and the cost of painting each house can go up to 20 -> 20 * n + 1 is greater than any total cost.
            avail_colors:Set[int] = {0, 1, 2} - {last_color}

            for color in avail_colors:
                curr_paint_cost:int = costs[from_house][color]
                min_paint_cost_next = get_min_paint_cost(from_house+1, color)
                min_paint_cost_curr = min(min_paint_cost_curr, curr_paint_cost + min_paint_cost_next)

            min_cost_from_house[(from_house, last_color)] = min_paint_cost_curr

            return min_cost_from_house[(from_house, last_color)]

        return get_min_paint_cost(0, -1)