# https://leetcode.com/problems/insert-interval/

from typing import List


def is_intercepted(i_1: List[int], i_2: List[int]) -> bool:
    return (i_1[0] <= i_2[0] and i_2[0] <= i_1[1]) or (i_2[0] <= i_1[0] and i_1[0] <= i_2[1])


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if len(intervals) < 1:
        return newInterval
    ans = []
    if newInterval[0] <= intervals[0][0]:
        intervals.insert(0, newInterval)
    elif intervals[-1][0] <= newInterval[0]:
        intervals.append(newInterval)
    else:
        for i in range(len(intervals) - 1):
            if intervals[i][0] <= newInterval[0] and newInterval[0] < intervals[i+1][1]:
                intervals.insert(i + 1, newInterval)

    ans.append(intervals[0])
    # Time to merge the intervals:
    for i in range(1, len(intervals)):
        if is_intercepted(ans[-1], intervals[i]):
            # merge them
            new_start = min(ans[-1][0], intervals[i][0])
            new_end = max(ans[-1][1], intervals[i][1])
            ans[-1] = (new_start, new_end)
            continue
        ans.append(intervals[i])

    return ans


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]

print("intervals = ", intervals)
print("new_interval = ", new_interval)
print("After merge: ", insert(intervals, new_interval))
