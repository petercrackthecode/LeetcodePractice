# https://leetcode.com/problems/largest-time-for-given-digits/
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort()
        ans = ""
        for first_h in [0, 1, 2]:
            for second_h in range(10):
                if first_h == 2 and second_h > 3:
                    break
                # 0 -> 5
                for first_m in range(6):
                    # 0 -> 9
                    for second_m in range(10):
                        time_digits = sorted([first_h, second_h, first_m, second_m])
                        if time_digits == arr:
                            new_time = f"{first_h}{second_h}:{first_m}{second_m}"
                            ans = max(ans, new_time)

        return ans
