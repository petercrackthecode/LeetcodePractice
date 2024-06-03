# https://leetcode.com/problems/ransom-note/
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Steps to solve the problem:
        1. Have a dictionary to save all the characters appeared in magazine and their frequencies where:
          - key: character.
          - value on that key: the number that characters appear in magazine
        2. Iterate through every character in ransomNote. Each time we do so, magazine[char] -= 1.
           - If not magazine.has_key(char) or magazine[char] < 0: return False immediately and stop the program.
        3. Returns true.
        """
        magazine_ch_count:Counter[str, int] = Counter(magazine)

        for ch in ransomNote:
            magazine_ch_count[ch] -= 1
            if magazine_ch_count[ch] < 0:
                return False


        return True