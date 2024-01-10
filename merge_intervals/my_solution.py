import functools
from typing import List
from collections import deque


class Solution:
    def proceed_two_intervals(self, a: List[int], b: List[int]) -> List[List[int]]:
        start_first = a if a[0] < b[0] else b
        start_last = a if a[0] >= b[0] else b

        # don't intersect
        if start_first[1] < start_last[0]:
            return [start_first, start_last]

        return [[start_first[0], max(start_first[1], start_last[1])]]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        output = [[1,6],[8,10],[15,18]]

        - two intervals intersect
        [1     9]
            [4     11]
        - one interval combines the other
        [1               20]
           [3         15]
        - two intervals don't intersect at all
        [1  3]
                 [5   15]

        - sort intervals by start_time. have a custom comparator function compare_by_start_time(a: List[int], b: List[int]) -> int to help us do so
        - put the first interval in intervals to output output = deque([intervals[0]])
        - for idx, interval in enumerate(intervals[1:]):
            last_interval_in_output = output.pop()
            output += self.proceed_two_intervals(last_interval_in_output, interval)
        - return output

        N = len(intervals)
        Time: O(N logN)
        Space: O(1)
        """
        def compare_by_start_time(a: List[int], b: List[int]) -> int:
            return a[0] - b[0]

        intervals.sort(key=functools.cmp_to_key(compare_by_start_time))
        output = deque([intervals[0]])

        for idx in range(1, len(intervals)):
            interval = intervals[idx]
            last_interval_in_output = output.pop()
            output += self.proceed_two_intervals(
                last_interval_in_output, interval)

        return list(output)
