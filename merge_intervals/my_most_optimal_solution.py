# https://leetcode.com/problems/merge-intervals/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        if we sort the interval by their start time, for two adjacent intervals at indices i and (i+1), there are only 3 cases:
            - no intersection: intervals[i][1] < intervals[i+1][0]
            - i covers (i+1): intervals[i][1] >= intervals[i+1][1]
            - intersection: intervals[i][1] >= intervals[i+1][0]

        - if the length of intervals is <= 1: return intervals
        - ans = []
        - sort intervals by start time
        - have a variable called curr_interval = intervals[0]
        - loop i from 1 to len(intervals) - 1:
            - get the intersection of curr_interval & intervals[i] using a helper function called merge_interval(i1: List[int], i2: List[int]) -> List[List[int]]. 
            - If the result of the merge is an array of 2 elements => we have 2 non-overlapping intervals:
                - append curr_interval to ans.
                - curr_interval is assigned to intervals[i]
                - if i equals len(intervals) - 1: append intervals[i] to ans.
            - otherwise: the result of the merge is an array of 1 element:
                - curr_interval is assigned to to the result of the merge.
                - if i equals len(intervals) - 1: append curr_interval to ans.
        - return ans

        Time: O(N log N) | N = len(intervals)
        Space: O(1)
        """
        if len(intervals) <= 1:
            return intervals
        ans = []
        intervals.sort()
        curr_interval = intervals[0]

        def merge_intervals(i1: List[int], i2: List[int]) -> List[List[int]]:
            if i1[1] < i2[0]:
                # no intersection
                return [i1, i2]
            elif i1[1] >= i2[1]:
                # covers
                return [i1]
            else:  # intersection
                return [[i1[0], i2[1]]]

        for i in range(1, len(intervals)):
            merged = merge_intervals(curr_interval, intervals[i])
            if len(merged) == 2:
                ans.append(curr_interval)
                curr_interval = intervals[i]
                if i == len(intervals) - 1:
                    ans.append(intervals[i])
            else:  # len(merged) == 1:
                curr_interval = merged[0]
                if i == len(intervals) - 1:
                    ans.append(curr_interval)

        return ans
