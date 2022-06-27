# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        characters_freq_in_s = dict()
        characters_freq_in_t = dict()

        for char in s:
            if char in characters_freq_in_s:
                characters_freq_in_s[char] += 1
            else:
                characters_freq_in_s[char] = 1

        for char in t:
            if char in characters_freq_in_t:
                characters_freq_in_t[char] += 1
            else:
                characters_freq_in_t[char] = 1

        for key in characters_freq_in_s:
            if (not key in characters_freq_in_t) or (characters_freq_in_s[key] != characters_freq_in_t[key]):
                return False

        return True
