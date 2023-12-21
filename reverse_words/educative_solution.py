# https://leetcode.com/problems/reverse-words-in-a-string/
import re
from typing import List


# A function that reverses a whole sentence character by character


def str_rev(_str: List[str], start_rev: int, end_rev: int):
    # Starting from the two ends of the list, and moving
    # in towards the center of the string, swap the characters
    while start_rev < end_rev:
        _str[start_rev], _str[end_rev] = _str[end_rev], _str[start_rev]
        start_rev += 1  # move forwards towards the middle
        end_rev -= 1  # move backwards towards the middle


def reverse_words(sentence: str) -> str:
    # remove leading, trailing, and multiple spaces
    sentence = re.sub(' +', ' ', sentence.strip())
    # We need to convert the updated string
    # to lists of characters as strings are immutable in Python
    sentence = list(sentence)
    str_len: int = len(sentence)

    # We will first reverse the entire string
    str_rev(sentence, 0, str_len - 1)
    # Now all the words are in the desired location, but
    # in reverse order: "Hello World" -> "dlroW olleH"
    start: int = 0
    end: int = 0

    # Now, let's iterate the reversed string and reverse each word in place.
    # "dlroW olleH" -> "World Hello"
    while start < str_len:
        # Find the end index of the word.
        while end < str_len and sentence[end] != ' ':
            end += 1
        # Let's call our helper function to reverse the word in-place
        str_rev(sentence, start, end-1)
        start = end + 1
        end += 1

    return ''.join(sentence)


word = reverse_words('Hello World')
print(word)
