# https://leetcode.com/problems/next-closest-time/
from typing import Set


class Solution:
    def nextClosestTime(self, time: str) -> str:
        """
        have a list of digits: digits
        generate all closing times from the given digits.
        19:34 -> 1, 3, 4, 9
        - 19:39
        - 13:49 (next day)
        - 14:

        - from the given time, generate all the next time from the curr_time: have a function called get_next_time(curr_time)
        - have another function called can_generate_time(curr_time: str) -> to check if a given time contains all only our digits.
        - keep generating times up to 1440 times until we have found a valid time (break the loop then)
        """

        digits: Set[str] = set([ch for ch in time if ch.isdigit()])

        curr_time = time
        count = 1440

        def get_next_time(curr_time: str) -> str:
            hr, minute = [int(num_str) for num_str in curr_time.split(":")]
            minute += 1
            if minute >= 60:
                minute = 0
                hr = (hr + 1) % 24

            hr_str = f"0{hr}" if hr < 10 else f"{hr}"
            min_str = f"0{minute}" if minute < 10 else f"{minute}"

            return f"{hr_str}:{min_str}"

        def can_generate_time(curr_time: str) -> str:
            nonlocal digits
            for ch in curr_time:
                if ch.isdigit():
                    if not ch in digits:
                        return False

            return True

        while count > 0:
            curr_time = get_next_time(curr_time)
            if can_generate_time(curr_time):
                return curr_time
            count -= 1

        return time
