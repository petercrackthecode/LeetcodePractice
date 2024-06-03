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
        char_freq = dict()
        for char in magazine:
            char_freq[char] = char_freq.get(char, 0) + 1

        for char in ransomNote:
            if not char_freq.has_key(char) or char_freq[char] - 1 < 0:
                return False
            char_freq[char] -= 1

        return True
