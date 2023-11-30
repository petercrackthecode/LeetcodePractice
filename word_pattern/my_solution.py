# https://leetcode.com/problems/word-pattern/
from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        important concept: bijection: one-to-one matching.

        split s into words delimited by a space (' '). call it s_words (remember to filter out empty strings)
        return False immediately if len(pattern) != len(s_words)
        have a dictionary called char_to_word (key: a character: str, value: a string matched with that character: str)
        loop through each character at index 0 -> len(pattern)-1:
        - if the character already exists as a key in char_to_word:
            if s_words[index] equals to char_to_word[char]: continue
            else: return False
        - otherwise, assign the key of char in char_to_word to the value of s_words[index]

        After the loop, return True
        """
        s_words = [word for word in s.split(' ') if word != ""]
        if len(pattern) != len(s_words):
            return False

        char_to_word = defaultdict(str)
        word_to_char = defaultdict(str)

        for i, char in enumerate(pattern):
            word = s_words[i]
            if char in char_to_word:
                if word != char_to_word[char] or word_to_char[word] != char:
                    return False
            else:
                if word in word_to_char:
                    return False
                char_to_word[char] = word
                word_to_char[word] = char

        return True
