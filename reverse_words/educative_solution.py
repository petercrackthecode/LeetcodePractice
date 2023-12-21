# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        - Reverse the entire string.
        - Start iterating over the reversed string using two pointers, start and end initially set at index 0.
        - While iterating over the string, when end points to a space, reverse the word pointed by start and end-1.
        - Once the word has been reversed, update the start and end to the start index of the next word.
        - Repeat the process until the entire string is iterated and return the string.
        """
        return ' '.join([word[::-1] for word in [w for w in s[::-1].split(' ') if w != '']])
