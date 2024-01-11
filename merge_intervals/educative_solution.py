# https://leetcode.com/problems/merge-intervals/
from typing import List


def merge_intervals(intervals: List[List[int]]):
    if not intervals:
        return None
    result = []
    result.append(intervals[0])
    for i in range(1, len(intervals)):
        last_added_interval = result[-1]
        curr_start = intervals[i][0]
        curr_end = intervals[i][1]
        prev_end = last_added_interval[1]

        if curr_start <= prev_end:
            result[-1][1] = max(curr_end, prev_end)
        else:
            result.append([curr_start, curr_end])
    return result
