# https://leetcode.com/problems/most-common-word/
from typing import List


def split_words(paragraph):
    word = ""
    words = []
    for char in paragraph:
        if (char == " " or char in "!?',;."):
            if word != "":
                words.append(word)
                word = ""
        else:
            word += char

    if word != "":
        words.append(word)

    return words


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Turn paragraph to lowercase and remove all punctuations
        paragraph = paragraph.lower()
        # use a set for fast lookup
        banned_set = set(banned)
        words = split_words(paragraph)
        most_frequent_and_valid_word = ""
        words_frequency = dict()

        for word in words:
            if not word in banned_set:
                words_frequency[word] = words_frequency.get(word, 0) + 1
                if words_frequency[word] > words_frequency.get(most_frequent_and_valid_word, 0):
                    most_frequent_and_valid_word = word

        return most_frequent_and_valid_word
