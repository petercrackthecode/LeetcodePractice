# https://leetcode.com/problems/interval-list-intersections/
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        firstList =  [[0,2],[5,10],[13,23],[24,25]]
        secondList = [[1,5],[8,12],[15,24],[25,26]]

        [1, 2], [5, 5] [8, 10], [15, 23], [24, 24], [25, 25]

        - ans = []
        - have two pointers i = j = 0 where i represents the firstList and j represents secondList
        - repeat these steps while i < len(firstList) and j < len(secondList):
            - if firstList[i] intercepts with secondList[j], append the interception range to ans.
            - if firstList[i]'s end time is earlier than secondList[j]'s end time: increment i by 1. Otherwise, increment j by 1.
        - return ans

        Time: O(M + N) | M = len(firstList), N = len(secondList)
        Space: O(1)
        """
        ans = []
        i = j = 0

        def is_intercepted(i1: List[int], i2: List[int]) -> bool:
            [start_before, start_after] = [
                i1, i2] if i1[0] <= i2[0] else [i2, i1]

            return start_before[0] <= start_after[0] <= start_before[1]

        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]
            if is_intercepted(first, second):
                ans.append([max(first[0], second[0]),
                           min(first[1], second[1])])
            # whichever interval has the earlier end_time has its pointer incremented by 1
            if first[1] <= second[1]:
                i += 1
            else:
                j += 1
        return ans
