# https://leetcode.com/problems/palindromic-substrings/
from typing import List


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        dp: List[List[int]] = [[False for _ in range(len(s))] for _ in range(len(s))]

        # all substrings of length 1 are palindromic
        for i in range(len(s)):
            dp[i][i] = True
            count += 1

        # all substrings of length 1 are palindromic if the first & the last characters are the same
        for i in range(len(s) - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            count += dp[i][i + 1]

        for length in range(3, len(s) + 1):
            i = 0
            for j in range(length - 1, len(s)):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                count += dp[i][j]
                i += 1

        return count
