# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        brute-force: have 2 pointers-
        s_idx which is used to iterate through s
        t_idx which is used to iterate through t
        s_idx = t_idx = 0
        iterate through s and t using s_idx & t_idx until one of two pointers (or both) hit the end of their respective strings
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
                t_idx += 1
            else:
                t_idx += 1
        return s_idx >= len(s)
        """
        s_idx = t_idx = 0
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
                t_idx += 1
            else:
                t_idx += 1
        return s_idx >= len(s)
