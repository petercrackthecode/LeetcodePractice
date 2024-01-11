# https://leetcode.com/problems/insert-interval/

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        new_interval = [newInterval[0], newInterval[1]]

        def findPivot(start, end, target):
            while start <= end:
                mid = (start + end) // 2
                if intervals[mid][0] <= target <= intervals[mid][1]:
                    return mid
                elif target > intervals[mid][0]:
                    start = mid + 1
                else:
                    end = mid - 1
            return start

        start_pivot = findPivot(0, n-1, newInterval[0])
        if start_pivot < n and intervals[start_pivot][0] <= newInterval[0] <= intervals[start_pivot][1]:
            new_interval[0] = intervals[start_pivot][0]
            new_interval[1] = max(intervals[start_pivot][1], newInterval[1])

        end_pivot = findPivot(0, n-1, newInterval[1])
        if end_pivot < n and intervals[end_pivot][0] <= newInterval[1] <= intervals[end_pivot][1]:
            new_interval[1] = intervals[end_pivot][1]
            end_pivot += 1

        intervals[start_pivot:end_pivot] = [new_interval]
        return intervals
