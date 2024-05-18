# https://leetcode.com/problems/word-break/description/
from typing import List, DefaultDict
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        - we can reuse the same word in wordDict multiple times.
        - return True if we can segment s using words in wordDict.
        - Otherwise, return False

        s        = 'leetcode' -> 'leet' + 'code'
        wordDict = ['leet', 'code']
        ans      = True

        s        = 'applepenapple' -> 'apple' + 'pen' + 'apple'
        wordDict = ["apple","pen"]
        ans      = True

        Bruteforce: loop thru each character in s:
                    *
        s        = 'leetcode'
        for each character ch at position i, see if we have the words in wordDict where:
            - word_length = len(word)
            - (i + word_length - 1) is smaller than len(s)
            - word is equal to s[i: i+word_length]
            - if i_word_length == len(s) => we have traversed thru all characters in string s and successfully broken s into words within wordDict (base case) => return True.

        - return False

        - have a helper function called word_break_helper(start: int) -> bool to help us recursively breaking current string into words
        - return word_break_helper(0)
        """
        can_form_subsequence_at_idx: DefaultDict[int, bool] = defaultdict(lambda: False)

        def word_break_helper(start: int) -> bool:
            nonlocal s, wordDict, can_form_subsequence_at_idx

            if start in can_form_subsequence_at_idx:  # memoized calculation
                return can_form_subsequence_at_idx[start]

            if start == len(s):  # we've exhausted all characters within s
                can_form_subsequence_at_idx[start] = True
            else:
                for word in wordDict:
                    word_length: int = len(word)
                    """
                                    *
                                01234567 | len(s) = 8
                    s        = 'leetcode' -> 'leet' + 'code'
                    wordDict = ['leet', 'code']
                    """
                    if (start + word_length - 1) < len(s) and word == s[
                        start : start + word_length
                    ]:  # adding the new word in wordDict to our current sequence should not make the sequence longer than s
                        new_start: int = start + word_length
                        can_form_subsequence_at_idx[start] = (
                            can_form_subsequence_at_idx[start]
                            or word_break_helper(new_start)
                        )

                        """
                        repeating subproblem: at a new start index. can we form a valid sequence whose strings combine to s[start:]
                        """

            return can_form_subsequence_at_idx[start]

        return word_break_helper(0)
