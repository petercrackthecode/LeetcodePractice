# https://leetcode.com/problems/isomorphic-strings/
from typing import DefaultDict
from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        - 2 strings s and t are isomorphic if the characters in s can be replaced to get t.
        - preserve the order of characters.
        - no 2 characters (x, y) can map to the same character ch.
        - ch can map to itself. ch = ch
        - return True if both strings are isomorphic, otherwise return False.

        s   = 'egg'
        t   = 'add'
        ans = True
        {
            'e': 'a',
            'g': 'd',
        }

        s   = 'foo'
        t   = 'bar'
        ans = False
        {
            'f': 'b',
            'o': 'a',
            'o': 'r'
        }
        => If a character ch already exists in a map with a character x (map_char[ch] = x),
        then it cannot be reassigned to a different character y.

                *
        s   = 'paper'
        t   = 'title'
        ans = True
        {
            'p': 't',
            'a': 'i',
            'e': 'l',
            's': 'l' => False | 'l' from t cannot be mapped to 2 different characters in s
            'r': 'e'
        }

        s and t must share the same length.
        each character ch_s in s can only map to one unique character in t
        each character ch_t in t can only map to one unique character in s

        => we need 2 dictionaries: s_to_t and t_to_s

        - check if s and t has the same length: if not, return False immediately.
        - have a dictionary to map each character in s to its corresponding character in t: s_to_t:DefaultDict[str, str] = defaultdict(str)
        - have a dictionary to map each character in t to its corresponding character in s: t_to_s:DefaultDict[str, str] = defaultdict(str)
        - loop thru each index i from 0 -> len(s)-1: for i in range(len(s)):
            - fetch the character at index i from s: ch_s:str = s[i]
            - fetch the character at index i from t: ch_t:str = t[i]
            #      *          *
            # s = "foo", t = "bar"
            - if both ch_s doesn't exists within s_to_t and ch_t doesn't exist within t_to_s (s_to_t[ch_s] == t_to_s[ch_t] == ''):
                - return False
            - otherwise, if s_to_t[ch_s] is different from ch_t or t_to_s[ch_t] is different from ch_s:
                - return False

            return True
        """
        if len(s) != len(t):
            return False
        s_to_t: DefaultDict[str, str] = defaultdict(str)
        t_to_s: DefaultDict[str, str] = defaultdict(str)

        for i in range(len(s)):
            ch_s: str = s[i]
            ch_t: str = t[i]

            # if both ch_s doesn't exist in s_to_t and ch_t doesn't exist in t_to_s => assign the characters to their corresponding dictionaries
            if s_to_t[ch_s] == t_to_s[ch_t] == "":
                s_to_t[ch_s] = ch_t
                t_to_s[ch_t] = ch_s
            elif s_to_t[ch_s] != ch_t or t_to_s[ch_t] != ch_s:
                return False

        return True
