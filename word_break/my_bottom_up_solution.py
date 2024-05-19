# https://leetcode.com/problems/word-break/
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        - Find all possible prefixes of the input string
        - For each prefix, check if it's contained in the dictionary.
        If it is, repeat the process with the rest of the string
        - For the remaining string, find all possible prefixes in the dictionary. Continue this process until
        the whole string has been processed.
        - After processing the whole string, return TRUE if it could be broken into space-separated dictionary
        words. Otherwise, return False.
        """

        """
             01234567
        s = "leetcode", wordDict = ["leet","code"]
        can_form_till_idx[0] = True
        can_form_till_idx[1] = False
        can_form_till_idx[2] = False
        can_form_till_idx[3] = False
        can_form_till_idx[4] = can_form_till_idx[4 - len('leet')] = True

                                                            0 -> len(s) (inclusively)
        - Have a list called can_form_till_idx:List[int] = [False for _ in range(len(s) + 1)] that given an index i within the string s: if we can form a valid sequence from substring s[:i], then can_form_till_idx[i] =  True. Otherwise, can_form_till_idx[i] = False.
        - base case: we don't need any words from wordDict to form an empty string -> can_form_till_idx[0] = True
        - the string s will span from index 0 -> len(s)-1
        - loop: from i = 1 -> len(s):
            - loop: for each word within wordDict:
                - check if word is a suffix of s[:i]: (s[:i].endswith(word))
                    - Yes: 
                        - can_form_till_idx[i] = can_form_till_idx[i - len(word) - 1]
                        - if can_form_till_idx[i] is True:
                            - break the loop since we have a happy case (we can form a valid subsequence from 0 -> i-1 in s)
        
        - return can_form_till_idx[len(s)]
        """
        can_form_till_idx: List[int] = [False for _ in range(len(s) + 1)]
        # base case: empty string -> can always be formed form wordDict
        can_form_till_idx[0] = True

        for i in range(1, len(s) + 1):
            curr_str: str = s[:i]

            for word in wordDict:
                if curr_str.endswith(word):  # len(curr_str) >= len(word)
                    can_form_till_idx[i] = can_form_till_idx[i - len(word)]
                    if can_form_till_idx[i]:
                        # we have a happy case of True -> we can form the current substring of s from words in wordDict -> drop further loop
                        break

        return can_form_till_idx[len(s)]
