# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if s.count(c) != t.count(c):
                return False

        return True
