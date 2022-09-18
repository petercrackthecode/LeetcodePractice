# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
from typing import List


def is_palindrome(word: str) -> bool:
    return word[0] == word[1]


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        + Traverse through every word in the words list.
        + At each step, revert the word, search if the reversed_word exists in a dictionary called words_frequency:
        - If yes and words_frequency[reversed_word] > 0:
          output += len(reversed_word)
          words_frequency[reversed_word] -= 1
          if is_palindrome(word) and words_frequency[word] == 0 and word in singly_palindromes:
            singly_palindromes.remove(word)
        - Otherwise:
            words_frequency[word] = words_frequency.get(word, 0) + 1
            if is_palindrome(word):
              singly_palindromes.add(word)
        - Exception: if the word is a palindrome itself, how are we going to deal with it?
          We can have a list to save all the palindromic words itself called singly_palindromes. in the end, we traverse
          through the list and find the longest word, then add its length to our output.
        - We should have a helper function called is_palindrome to check if a word is palindromic.
        """
        singly_palindromes = set()
        words_frequency = dict()
        output = 0

        for word in words:
            reversed_word = word[::-1]
            if words_frequency.get(reversed_word, 0) > 0:
                # multiply by 2 since we have word and reversed_word added to our output.
                output += (len(reversed_word) * 2)
                words_frequency[reversed_word] -= 1
                if is_palindrome(word) and words_frequency[word] == 0 and word in singly_palindromes:
                    singly_palindromes.remove(word)
            else:
                words_frequency[word] = words_frequency.get(word, 0) + 1
                if is_palindrome(word):
                    singly_palindromes.add(word)
        longest_palindrome = ''
        for palindrome in singly_palindromes:
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome
        output += len(longest_palindrome)

        return output
