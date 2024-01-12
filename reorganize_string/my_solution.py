# https://leetcode.com/problems/reorganize-string/
from collections import defaultdict
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        - have a dictionary to save the frequencies of each character ch in s: ch_freq = defaultdict(int)
        - have a heap called next_chars that save the pairs of (neg_freq, character) (negative frequency since heap is min heap in python). Iterate thru ch_freq to populate next_chars.
        - have a variable called prev_pair to save the previous pair of (freq, character) that we've just added to ans. prev_pair initialized to None.

        - repeat these steps while next_chars is not empty:
            - pop the pair (neg_freq, character) whose character has the highest frequency from next_chars. save it to temp = heappop(next_chars)
            - negate neg_freq to get the true frequency of the character: freq = -neg_freq: temp = (-temp[0], temp[1])
            - if next_chars is empty after the pop and the frequency freq of the current character is greater than 1: we return an empty string "" (because there's no possible arrangement)
            - decrement the frequency of the character we've just pushed by 1: temp = (temp[0] - 1, temp[1])
            - if prev_pair is not null, we push prev_pair to next_chars.
            - if the frequency of the character from temp is not 0 (we still have characters of that type to push to ans), prev_pair = temp. Otherwise, prev_pair = null.

        return ans

        Time: O(N) + O(1) = O(N) | N = len(s)
        Space: O(1)
        """
        ch_freq = defaultdict(int)
        next_chars = []
        prev_pair = None
        ans = []

        for ch in s:
            ch_freq[ch] += 1

        for ch, freq in ch_freq.items():
            heappush(next_chars, (-freq, ch))

        while len(next_chars) > 0:
            temp = heappop(next_chars)
            # negate and decrement by 1
            temp = (-temp[0] - 1, temp[1])
            ans.append(temp[1])

            if prev_pair and prev_pair[0] > 0:
                heappush(next_chars, (-prev_pair[0], prev_pair[1]))

            prev_pair = temp if temp[0] > 0 else None

            if len(next_chars) <= 0 and temp[0] >= 1:
                return ""

        return ''.join(ans)
