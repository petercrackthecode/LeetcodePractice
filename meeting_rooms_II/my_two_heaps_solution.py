# https://leetcode.com/problems/meeting-rooms-ii/
from heapq import heappush, heappop
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        - ans:int = 0
        - have 2 min heaps: meetings (List[Tuple[int, int]]) and running_meeting_endtimes (List[int]). tasks save the tuple within intervals where running_meeting_endtimes save the end times of ongoing meetings.
        - loop: for each interval in intervals: add interval to meetings

        - loop: while meetings is none-empty:
            - pop a pair of meeting's (start, end) from meetings
            - while running_meeting_endtimes is not empty and the earliest end time of meetings within running_meeting_endtimes (aka the heap's top) is smaller than or equal to start:
                - pop an element from the heap running_meeting_endtimes

            - push the end time to the heap running_meeting_endtimes
            - assign: ans = max(ans, len(running_meeting_endtimes))

        - return ans
        """
        ans: int = 0
        meetings: List[List[int]] = []
        running_meeting_endtimes: List[int] = []

        for interval in intervals:
            heappush(meetings, interval)

        while bool(meetings):
            start, end = heappop(meetings)
            while bool(running_meeting_endtimes) and running_meeting_endtimes[0] <= start:
                heappop(running_meeting_endtimes)
            heappush(running_meeting_endtimes, end)

            ans = max(ans, len(running_meeting_endtimes))

        return ans
