# https://leetcode.com/problems/minimum-window-subsequence/
from collections import deque


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        """
        - Begin iterating through str1 to locate a potential window that contains all the characters of str2 in their order of appearance.
        - Once you’ve identified a potential end, backtrack through the characters of str1 from this end position until you’ve found all the characters of str2 in reverse order. This helps locate the potential start of the smallest subsequence.
        - Update the minimum window subsequence if the current window is smaller than the shortest subsequence found so far.
        - Repeat the process, starting every time from the second character of the current window, until the end of str1 has been reached.
        - Return the minimum window subsequence.

        have a pointer p pointing to the current character in s2. p = 0
        have 2 pointers left and right.
        left = 0
        increment left by 1 while s1[left] is different from s2[p]
        assign: right is equal to left
        loop: while right < len(s1) and p < len(s2):
            if s1[right] is equal to s2[p], increment p by 1
            increment right by 1
        if p is greater than or equal to len(s2) => we have a valid window:
            - backtrack to get the minimum contiguous substring, then assign the result to ans if its length is smaller than ans. Have a helper function call backtrack(left, right) to help you do so. Then, reassign 0 to p.
            - move left to the next character in s1 that is equal to s2[0]
        """
        p = 0
        left = 0
        ans = " " * (len(s1) + 1)

        def backtrack(left: int, right: int) -> None:
            nonlocal s1, s2, ans
            # print('valid_str = ', s1[left:right+1])
            characters_to_check = deque(s2)
            i = right
            while i >= left:
                if s1[i] == characters_to_check[-1]:
                    characters_to_check.pop()
                if len(characters_to_check) == 0:
                    # print('valid substr of substring = ', s1[i:right+1])
                    ans = s1[i:right+1] if right + 1 - i < len(ans) else ans
                    break

                i -= 1

            if i < left:
                ans = s1[left:right+1] if right + 1 - left < len(s1) else ans

            # print("___________________________________")

        while left < len(s1) and s1[left] != s2[p]:
            left += 1
        right = left

        while right < len(s1) and p < len(s2):
            if s1[right] == s2[p]:
                p += 1
            if p >= len(s2):
                # the substring from left -> right is guaranteed to has p2 as a subsequence.
                # we just need to find the shortest substring within [left, right] that also contains p2 as a subsequence.
                backtrack(left, right)
                p = 0
                left += 1
                while left < len(s1) and s1[left] != s2[p]:
                    left += 1
                    right = left
                right = left
            else:
                right += 1

        return "" if len(ans) > len(s1) else ans
