# https://leetcode.com/problems/maximize-distance-to-closest-person/
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        seats[i] == 1: occupied
                 == 0: empty

         0. 1. 2. 3. 4. 5. 6  7  8  
        [0, 0, 0, 1, 0, 0, 0, 0, 1]
        [0, 0, 1, 1, 1, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0, 0, 0, 0]

        - have a variable caled last_occupied_seat: int to save the index of the last seat where seats[last_occupied_seat] == 1
        - iterate through seats:

            - each time we find a seats[i] == 1:
                - calculate the distance between Alex to the nearest person if he would sit at the current range.
                - left = last_occupied_seat + 1
                - right = i-1
                - closest_dist = 0
                - if last_occupied_seat == -1:
                    closest_dist = i
                  else:
                    closest_dist = (right - left) // 2 + 1
                  output = max(output, closest_dist)
        """
        last_occupied_seat = -1
        output = 0

        for i, seat in enumerate(seats):
            if seat == 1:
                left = last_occupied_seat + 1
                right = i-1
                closest_dist = 0
                if last_occupied_seat == -1:
                    closest_dist = i
                else:
                    closest_dist = (right - left) // 2 + 1
                output = max(output, closest_dist)
                last_occupied_seat = i
            elif i == len(seats) - 1:  # seat == 0
                closest_dist = i - last_occupied_seat
                output = max(output, closest_dist)

        return output
