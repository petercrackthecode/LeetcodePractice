# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        w_count = Counter(words)

        two_count = 0
        center = 0
        four_count = 0

        for word, count in w_count.items():
            if word[0] == word[1]:
                # if there are 3 aa words we can only use 2
                two_count += count // 2 * 2

                if count % 2 == 1:
                    center = 2
            else:
                four_count += min(w_count[word], w_count[word[::-1]]) * 0.5

        return two_count*2 + int(four_count)*4 + center
