# https://leetcode.com/problems/boats-to-save-people/
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        each boat can carry at most 2 people

        people = [3,2,2,1]
        limit = 4
        [1, 2, 2, 3]
        out = 2

        remaining_space

        people = [3,5,3,4]

                    lr
        sorted = [3,3,4,5]
        limit = 6
        out = 3

        - sort the people list ascendingly: people = sorted(people)
        - have 2 pointer- left and right = [0, len(people) - 1]
        - for each heavy person (people[right]), see if we can match a light person with 'em (people[right] + people[left] <= limit):
            - yes: increment left by 1
            - no: 
            decrement right by 1
            increment boat_count by 1
        - repeat the above while left <= right
        """
        sorted_people = sorted(people)
        [left, right] = [0, len(sorted_people) - 1]
        boats_count = 0

        while left <= right:
            if sorted_people[right] + sorted_people[left] <= limit:
                left += 1
            right -= 1
            boats_count += 1

        return boats_count
