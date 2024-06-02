# https://leetcode.com/problems/car-fleet/
from typing import List, Tuple

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        target   = 12
        position = [10, 8, 0, 5, 3]
        speed    = [2,  4, 1, 1, 3]
        output   =  3

        once two or more cars become a fleet, they drive at the same speed. The faster car will slow down to match the slower car's speed.

        target   = 100
        position = [0, 2, 4]
        speed    = [4, 2, 1]

        1:              2:          3:
        0 -> 4 (+4)   | 6 (+2)   |  7 (+1)
        2 -> 4 (+2)   | 6 (+2)   |  7 (+1)
        4 -> 5 (+1)   | 6 (+1)   |  7 (+1)

        once 2 cars' positions match at any point in time, they join each other as 1 car and inherit the slowest speed.
        '''
        # (pos, speed)
        pos_and_speed:List[Tuple[int, int]] = []

        for i, curr_pos in enumerate(position):
            curr_speed:int = speed[i]
            pos_and_speed.append((curr_pos, curr_speed))

        pos_and_speed.sort(reverse=True)

        # (pos, speed)
        car_fleet:List[Tuple[int, int]] = []

        for (pos, speed) in pos_and_speed:
            if len(car_fleet) == 0: # empty car_fleet -> create a new car_fleet
                car_fleet.append((pos, speed))
                continue

            prev_car_pos, prev_car_speed = car_fleet[-1]
            '''
                2.3     2.5     3
            [(3, 3), (5, 2), (7, 1)]
            target = 10
            '''
            prev_time_to_reach_target:float = (target - prev_car_pos) / prev_car_speed
            curr_time_to_reach_target:float = (target - pos) / speed

            if prev_time_to_reach_target < curr_time_to_reach_target: # 2 cars are not going to merge together into a car fleet since the current car won't reach the prev_car at any point -> append a new car_fleet into our stack
                car_fleet.append((pos, speed))

        return len(car_fleet)
        '''
        - when can 2 cars be merged together?
            - target
            - car1: (p1, s1) - d1: (target - p1) / s1
            - car2: (p2, s2) - d2: (target - p2) / s2
            - if d2 <= d1: car2 at some point will catch up to car1 & 2 cars become a car fleet => merge them together.
        '''