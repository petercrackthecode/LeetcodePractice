# https://leetcode.com/problems/minimum-window-substring/
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        convert all the characters in t into a set called 
        count the character frequencies in t
        For a substr in s is valid, for each character ch in t, the ch's frequency in s must be greater than or equal to ch's frequency in t.

        ADOBECODEBANC

        sliding window technique: 
        ans = " " x (len(s) + 1)
        have a variable called valid_count to track the number of valid characters within our current substr (valid character ch: freq_substr[ch] >= freq_t[ch]). initialize valid_count to 0
        freq_t = defaultdict(int)
        freq_substr = defaultdict(int)
        iterate thru every character ch in t and increment freq_t[ch] by 1
        have two pointers: left and right, both initialized to -1

        loop these steps while left <= right and right < len(s):
        - if valid_count is greater than or equal to len(freq_t):
            - ans = ans if (right - left + 1 < len(ans)) else s[left:right+1]
        - if valid_count is smaller than len(freq_t): expand right:
            - increment right by 1.
            - if right is smaller than s's length:
                ch = s[right]
                increment freq_substr[right] by 1
                if freq_substr[ch] is equal to freq_t[ch]: increment valid_count by 1.
        - otherwise (valid_count >= len(freq_t) => we have a valid substring): expand left:
            - if left == -1: assigned 0 to left
            - ch = s[left]
            - decrement freq_substr[ch] by 1
            - if freq_substr[ch] is equal to (freq_t[ch] - 1): decrement valid_count by 1.
            - increment left by 1.
        """
        ans = " " * (len(s) + 1)
        freq_t = defaultdict(int)
        freq_substr = defaultdict(int)
        valid_count = 0

        for ch in t:
            freq_t[ch] += 1
        left = right = -1
        unique_ch_in_t = len(freq_t)

        while left <= right and right < len(s):
            if valid_count >= unique_ch_in_t:
                left_bound = 0 if left == -1 else left
                ans = s[left_bound:right +
                        1] if len(ans) > right - left_bound + 1 else ans

            if valid_count < unique_ch_in_t:
                right += 1
                if right < len(s):
                    ch = s[right]
                    freq_substr[ch] += 1
                    if freq_substr[ch] == freq_t[ch]:
                        valid_count += 1
            else:  # valid_count >= unique_ch_in_t
                if left == -1:
                    left = 0
                ch = s[left]
                freq_substr[ch] -= 1
                if freq_substr[ch] == freq_t[ch] - 1:
                    valid_count -= 1
                left += 1

        return "" if len(ans) > len(s) else ans
