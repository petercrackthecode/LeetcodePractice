# https://leetcode.com/problems/valid-word-abbreviation/
from typing import List


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        - no substring can be empty (no leading zeroes)
        - no 2 replaced substrings should be next to each other.
        substitution

        s ubstitutio n = s10n
        sub stit u tion = sub4u4
        substitution = 12
        su bst i t u ti on = su3i1u2on

        - abbr is a potential abbreviation
        - word is the original string.
        return if abbr is an abbreviation of word

                 i
        word = i nternational ization
        abbr = i12iz4n
                     j

                 i
        word2 = interna
                0123456
         i
        abc
        a2
         j
        curr_num = 2

            i = 4
        abbc
        0123
        a2c
          j
        curr_num = 0
         i
        ab | len = 2
         j
        a1

        a12

        expand

        """
        expanded: List[str] = []
        curr_num: int = 0

        for i, ch in enumerate(abbr):
            if ch.isdigit():
                digit: int = int(ch)
                if digit == 0 and curr_num == 0:  # leading zero
                    return False
                curr_num = curr_num * 10 + digit
                if curr_num > 20:
                    return False
            else:  # not a digit
                for _ in range(curr_num):
                    expanded.append("#")
                curr_num = 0
                expanded.append(ch)

        for _ in range(curr_num):
            expanded.append("#")

        if len(word) != len(expanded):
            return False
        # word and expanded has the same length
        for i, ch in enumerate(word):
            expanded_ch: str = expanded[i]
            if expanded_ch != "#" and expanded_ch != ch:
                return False

        return True
