# https://leetcode.com/problems/palindromic-substrings/
from typing import DefaultDict, Tuple
from collections import defaultdict


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        - if a string s has length of len(s), then the result will be at least len(s)
        - A string is a palindrome when it reads the same backward as forward.
        - A string can has odd length of even length.
        - a string whose length is <= 1 is palindromic.

        how many substring can be formed from N = 1,000

        N^2
                           012
        s               = 'aaa'

        length 1 strings: 'a','a','a'
        length 2 strings: 'aa','aa'
        length 3 strings: 'aaa'

        for a substring from i -> j (inclusively). This string is a palindrome if:
        - s[i] == s[j]
        - s[i+1:j-1] is a palindrome => overlapping subproblems.

        ** STRATEGY **
        - ans:int = 0
        - have dictionary called is_palindrome_substr:DefaultDict[Tuple[int, int], bool] = defaultdict(lambda: False) that given a start and an end index (Tuple[int, int]), return True if the substring within the given range is a palindrome, otherwise, return False.
        - loop: for i in range(len(s)):
            - is_palindrome_substr[(i, i)] = True
        #  *
        # 012
        # aaa | len(s) = 3 | size = 2
        - loop: for size in range(1, len(s)+1):
            - for start in range(len(s) - size + 1):
                - end = start + size - 1
                - if s[start] equals s[end]:
                    - if start+1 <= end-1:
                        - assign: is_palindrome_substr[(start, end)] = is_palindrome_substr[(start+1, end-1)]
                    - otherwise: is_palindrome_substr[(start, end)] = True
                - otherwise, assign: is_palindrome_substr[(start, end)] = False

                - if is_palindrome_substr[(start, end)] is True: increment ans by 1

        *** ANALYSIS ***
        Time: O(N)
        Space: O(N)
        """
        ans: int = 0
        is_palindrome_substr: DefaultDict[Tuple[int, int], bool] = defaultdict(
            lambda: False
        )

        for size in range(1, len(s) + 1):
            for start in range(len(s) - size + 1):
                end: int = start + size - 1
                if s[start] == s[end]:
                    if start + 1 <= end - 1:
                        is_palindrome_substr[(start, end)] = is_palindrome_substr[
                            (start + 1, end - 1)
                        ]
                    else:
                        is_palindrome_substr[(start, end)] = True
                else:
                    is_palindrome_substr[(start, end)] = False

                if is_palindrome_substr[(start, end)]:
                    ans += 1

        return ans
