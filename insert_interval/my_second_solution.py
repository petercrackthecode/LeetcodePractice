# https://leetcode.com/problems/insert-interval/
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        - ans = []
        - have a helper function called merge_interval(i1: List[int], i2: List[int]) to help us attempt to merge two intervals (return an array of one interval if i1 and i2 are mergeable, otherwise return [i1, i2])
        - i = 0
        - loop thru intervals while i < len(intervals):
            - if intervals[i] intersects with newInterval, append the result interval to ans & terminate the loop.
            - otherwise, add intervals[i] to ans.
            - increment i by 1.

        return ans + intervals[i+1:]
        """
        if len(intervals) == 0:
            return [new_interval]
        elif new_interval[1] < intervals[0][0]:
            # push before first
            return [new_interval] + intervals
        elif intervals[-1][1] < new_interval[0]:
            # push after last
            return intervals + [new_interval]

        ans = []
        i = 0

        def merge_intervals(i1: List[int], i2: List[int]) -> List[int]:
            start = min(i1[0], i2[0])
            end = max(i1[1], i2[1])
            return [start, end]

        while i < len(intervals):
            # print('ans = ', ans, ', new_interval = ', new_interval)
            curr_interval = intervals[i]
            if curr_interval[1] < new_interval[0]:
                ans.append(curr_interval)
            elif new_interval[1] < curr_interval[0]:
                ans.append(new_interval)
                return ans + intervals[i:]
            else:  # overlap => merge
                new_interval = merge_intervals(curr_interval, new_interval)
                if i == len(intervals) - 1:
                    ans.append(new_interval)
            i += 1

        return ans
