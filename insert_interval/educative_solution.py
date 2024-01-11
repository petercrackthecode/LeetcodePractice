# https://leetcode.com/problems/insert-interval/
from typing import List


def insert_interval(existing_intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    new_start, new_end = new_interval[0], new_interval[1]
    i = 0
    n = len(existing_intervals)
    output = []
    while i < n and existing_intervals[i][0] < new_start:
        output.append(existing_intervals[i])
        i = i + 1
    if not output or output[-1][1] < new_start:
        output.append(new_interval)
    else:
        output[-1][1] = max(output[-1][1], new_end)
    while i < n:
        ei = existing_intervals[i]
        start, end = ei[0], ei[1]
        if output[-1][1] < start:
            output.append(ei)
        else:
            output[-1][1] = max(output[-1][1], end)
        i += 1
    return output
