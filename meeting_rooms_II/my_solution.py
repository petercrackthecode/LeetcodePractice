# https://leetcode.com/problems/meeting-rooms-ii/
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        [0   ,  .              .          30]
           [5,  .   10],
                          [15, .   20]

        [0,        5]
                  [5,          10]

        Original number of meetings needed = 0
        Meetings(0) = +1 = 1
        Meetings(5) = +1 = 2
        Meetings(10) = -1 = 1
        Meetings(15) = +1 = 2
        Meetings(20) = -1 = 1
        Meetings(30) = -1 = 0

        - have a variable called ans = 0
        - save the timeblocks as the format (timestamp: int, is_start_time: bool)
        - have a list to save all the time called sorted_time: List[Tuple[int, bool]]
        - Iterate thru intervals: for each [start, end] in intervals:
            - append (start, True) to sorted_time.
            - append (end, False) to sorted_time
        - Sort sorted_time
        - have a variable called curr_meetings_needed to track the number of ongoing meetings. curr_meetings_needed = 0
        - loop thru each pair (timestamp, is_start_time) in sorted_time:
            - if is_start_time:
                - curr_meetings_needed is incremented by 1
                - ans = max(ans, curr_meeting_needed)
            - otherwise, curr_meetings_needed is decremented by 1.
        - return ans

        Time: O(NlogN)
        Space: O(2N) = O(N)
        """
        ans = 0
        sorted_time = []

        for [start, end] in intervals:
            sorted_time.append((start, True))
            sorted_time.append((end, False))

        sorted_time.sort()
        curr_meetings_needed = 0

        for (_, is_start_time) in sorted_time:
            if is_start_time:
                curr_meetings_needed += 1
                ans = max(ans, curr_meetings_needed)
            else:
                curr_meetings_needed -= 1

        return ans
