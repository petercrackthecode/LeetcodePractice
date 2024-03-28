# https://leetcode.com/problems/meeting-rooms-ii/
from heapq import heappush, heappop
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        *** LOGIC ***
        - If we have a new meeting to run, see if by that meeting's start_time, we can remove any finished meeting
        from our running_meeting_endtimes heap (tracked by their end_times)
        - Then, add the new meeting's end time to running_meeting_endtimes.
        - Basically, when we have a new meeting to run, is there some meetings that already finishes?
            - If yes, we remove those finished meetings' room and allocate one of 'em to our new meeting.
            - No: we allocate a new room to our new meeting, increment our total rooms needed for these meetings by 1.

        *** STEPS ***
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
