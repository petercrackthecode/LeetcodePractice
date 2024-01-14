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
        - trimed out ans[0] if len(ans) > 0 and ans[0][0] == -inf
        - trimmed out ans[-1] if len(ans) > 0 and ans[-1][1] == inf

        schedule = [
            [
                [1,2],[5,6] -> [[-inf, 1], [2, 5], [6, inf]]
            ],
            [ [1,3] ], -> [[-inf, 1], [3, inf]]
            [ [4,10] ] -> [[-inf, 4], [10, inf]]
        ]

        [[-inf, 1], [2, 5], [6, inf]]
        [[-inf, 1], [3, inf]]

        [[-inf, 1], [3, 5], [6, inf]]
        [[-inf, 4], [10, inf]]

        [[-inf, 1], [3, 4], [10, inf]]
        """
        def get_free_time(intervals):
            if len(intervals) == 0:
                return []

            ans = [[float('-inf'), intervals[0][0]]]

            for i in range(1, len(intervals)):
                prev_interval = intervals[i-1]
                curr_interval = intervals[i]
                ans.append([prev_interval[1], curr_interval[0]])

            return ans + [[intervals[-1][1], float('inf')]]

        def intersected_intervals(group_1, group_2):
            i = j = 0
            ans = []
            while i < len(group_1) and j < len(group_2):
                i1 = group_1[i]
                i2 = group_2[j]
                # print('i1 = ', i1)
                # print('i2 = ', i2)
                # is_intersected?
                # if i1.start <= i2.start <= i1.end or i2.start <= i1.start <= i2.end:
                if i1[0] <= i2[0] <= i1[1] or i2[0] <= i1[0] <= i2[1]:
                    # intersected = Interval(max(i1.start, i2.start), min(i1.end, i2.end))
                    intersected = [max(i1[0], i2[0]), min(i1[1], i2[1])]
                    ans.append(intersected)
                # if i1.end <= i2.end:
                if i1[1] <= i2[1]:
                    i += 1
                else:
                    j += 1
            return ans

        def translate_schedule(schedule) -> List[List[List[int]]]:
            ans = []

            for employee in schedule:
                intervals = []
                for interval in employee:
                    start = interval.start
                    end = interval.end
                    intervals.append([start, end])
                ans.append(intervals)
            return ans

        def translate_list(intervals: List[List[int]]) -> List[Interval]:
            ans = []

            for interval in intervals:
                ans.append(Interval(interval[0], interval[1]))

            return ans

        ans = []
        translated_schedule = translate_schedule(schedule)

        # print('schedule = ', schedule)

        for employee in translated_schedule:
            free_time = get_free_time(employee)
            # print('ans = ', ans)
            # print('free_time = ', free_time)
            ans = free_time if not bool(
                ans) else intersected_intervals(ans, free_time)

        ans = [interval for interval in ans if interval[0] != float(
            '-inf') and interval[1] != float('inf') and interval[0] < interval[1]]

        return translate_list(ans)
