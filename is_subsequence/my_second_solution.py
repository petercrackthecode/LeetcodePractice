# https://leetcode.com/problems/is-subsequence/
from typing import Set
from collections import deque


class Solution:
    def get_subsequences(self, t: str) -> Set[str]:
        """
        - try deleting 0..len(t) characters from t to get the subsequences.
        t = "ahbgdc"
        0: ahbgdc
        1: hbgdc, abgdc, ahgdc, ahbdc, ahbgc, ahbgd
        2:
        3:

        have 2 queue: curr_subsequences & next_subsequences.
        ans = set()
        curr_subsequences = deque([t])
        while len(curr_subsequences) > 0:
            subsequence = curr_subsequences.popleft()
            ans.add(subsequence)
            for idx in range(len(subsequence))
                new_smaller_subsequence = subsequence[0:idx] + subsequence[idx+1:]
                curr_subsequences.append(new_smaller_subsequence)

        return ans
        """
        ans = set()
        curr_subsequences = deque([t])
        while len(curr_subsequences) > 0:
            subsequence = curr_subsequences.popleft()
            ans.add(subsequence)
            for idx in range(len(subsequence)):
                new_smaller_subsequence = subsequence[0:idx] + \
                    subsequence[idx+1:]
                curr_subsequences.append(new_smaller_subsequence)

        return ans

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        solution 2 to solve the followup case:
        - generate all subsequences of t & save them to a set: subsequences. Have a helper function called get_subsequences(t: str) -> Set[str] to help us do so
        - return s in subsequences
        """
        subsequences = self.get_subsequences(t)

        return s in subsequences
