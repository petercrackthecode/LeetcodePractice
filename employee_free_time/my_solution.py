# https://leetcode.com/problems/employee-free-time/
from typing import List

# Definition for an Interval.


class Interval:
    def __init__(self, start: int = -1, end: int = -1):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        """
        schedule = [
            [[1,2],[5,6]], -> [[-inf, 1], [2, 5], [6, inf]]
            [[1,3]], -> [[-inf, 1], [3, inf]]
            [[4,10]] -> [[-inf, 4], [10, inf]]
        ]

        output = [[3, 4]]

        - have ans = []
        - iterate thru each interval_group within schedule and do this step:
            - get the free time of each interval_group using a helper function get_free_time(i_group: List[List[int]]) -> List[List[int]]: free_time = get_free_time(interval_group)
            - if ans is an empty list, ans = free_time
            - otherwise, ans is assigned to intersected_intervals(ans, free_time)
        - trimed out ans[0] if ans[0][0] == -inf
        - trimmed out ans[-1] if ans[-1][1] == inf
        """
