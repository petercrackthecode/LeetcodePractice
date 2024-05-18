# https://leetcode.com/problems/isomorphic-strings/
from typing import Dict


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
        - have a dictionary to map each character in s to its corresponding character in t: s_to_t:Dict[str, str] = dict()
        - have a dictionary to map each character in t to its corresponding character in s: t_to_s:Dict[str, str] = dict()
        - loop thru each index i from 0 -> len(s)-1: for i in range(len(s)):
            - fetch the character at index i from s: ch_s:str = s[i]
            - fetch the character at index i from t: ch_t:str = t[i]
            #      *          *
            # s = "foo", t = "bar"
            - one to one mapping: if ch_s exists in s_to_t but ch_t doesn't exist in t_to_s:
                - return False
            - otherwise, if ch_t exists in t_to_s but ch_s doesn't exist within s_to_t:
                - return False
            - otherwise, if both ch_t doesn't exist in t_to_s and ch_s doesn't exist within s_to_t:
                - update the map:
                    - assign: s_to_t[ch_s] = ch_t
                    - assign: t_to_s[ch_t] = ch_s
        *************************
            - otherwise, both ch_t exists in t_to_s and ch_s exists within s_to_t:
                - if s_to_t[ch_s] is different from ch_t or t_to_s[ch_t] is different from ch_s:
                    return False

            return True
        """
        if len(s) != len(t):
            return False
        s_to_t: Dict[str, str] = dict()
        t_to_s: Dict[str, str] = dict()

        for i in range(len(s)):
            ch_s: str = s[i]
            ch_t: str = t[i]

            if ch_s in s_to_t and not (ch_t in t_to_s):
                # print(f's_to_t = {s_to_t}')
                # print(f't_to_s = {t_to_s}')
                # print()
                return False
            elif ch_t in t_to_s and not (ch_s in s_to_t):
                # print(f's_to_t = {s_to_t}')
                # print(f't_to_s = {t_to_s}')
                # print()
                return False
            elif not (ch_t in t_to_s) and not (ch_s in s_to_t):
                s_to_t[ch_s] = ch_t
                t_to_s[ch_t] = ch_s
            else:  # ch_s exists within s_to_t and ch_t exists within t_to_s
                if s_to_t[ch_s] != ch_t or t_to_s[ch_t] != ch_s:
                    # print(f's_to_t = {s_to_t}')
                    # print(f't_to_s = {t_to_s}')
                    # print()
                    return False

        return True
