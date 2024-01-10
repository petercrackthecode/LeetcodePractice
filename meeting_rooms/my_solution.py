# https://leetcode.com/problems/meeting-rooms/
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Sort meetings by start time
        loop thru intervals, get the latest end_time.
        - if there is a meeting that with the start_time that is earlier than the latest end_time so far, we have a meeting time collision => we can't attend all meetings => return False immediately.

        return True
        """
        intervals.sort()
        latest_end_time = -1
        for [start, end] in intervals:
            if start < latest_end_time:
                return False
            latest_end_time = max(latest_end_time, end)

        return True
