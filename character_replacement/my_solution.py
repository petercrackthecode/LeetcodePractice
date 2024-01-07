# https://leetcode.com/problems/longest-repeating-character-replacement/
from collections import defaultdict
from typing import DefaultDict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        ABAB k = 2
        output = 4
        l
            r
        ABABC
        0123

        diff_factor = 0 -> 1 -> 1 -> 2 -> 3
        valid subwindow = diff_factor <= k
        {A: 1} -> {A: 1. B: 1} -> {A: 2, B: 1} -> {A: 2, B: 2} -> {A: 2, B: 2, C: 1}

        - diff_factor- minimum number of characters we must change within the current substring to get the string with one repeating character.
        - how to calculate diff_factor: the sum of all the frequencies of the non-most popular character.
        - Everytime the diff_factor > k, move the left pointer, update our dictionary & recalculate the diff_factor until the diff_factor == k. What if left == right. How do we extend it? then, we have to blindly increment right by 1.
        - If the diff_factor <= k:
            - ans = max(ans, right - left + 1)
            - extend the right pointer.

        Use a heap with 2 pairs to store the frequency of a character and a character.
        heap = [(2, A), (2, B), (1, C)]
        - have a helper function called get_diff_factor(heap: Dict[str, int]) -> int, to help us calculate the diff factor from our heap.
        """
        left = right = 0
        ans = 0
        ch_freq = defaultdict(int)
        ch_freq[s[0]] = 1

        def get_diff_factor(ch_freq: DefaultDict[str, int]) -> int:
            nonlocal left, right
            if len(ch_freq.keys()) < 2:
                return 0
            most_frequent_ch = ''
            freq_sum = right - left + 1

            for ch, freq in ch_freq.items():
                if most_frequent_ch not in ch_freq:
                    most_frequent_ch = ch
                elif freq > ch_freq[most_frequent_ch]:
                    most_frequent_ch = ch

            return freq_sum - ch_freq[most_frequent_ch]

        while left <= right and right < len(s):
            diff_factor = get_diff_factor(ch_freq)
            if diff_factor > k:
                ch_freq[s[left]] -= 1
                left += 1
                if left > right and right < len(s):
                    right += 1
                    ch_freq[s[right]] += 1
            else:  # diff_factor <= k => we can transform the entire string to be a string of repeating character.
                ans = max(ans, right - left + 1)
                right += 1
                if right < len(s):
                    ch_freq[s[right]] += 1

        return ans
