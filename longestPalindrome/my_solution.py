# https://leetcode.com/problems/longest-palindrome/
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Algorithm: 
          + get the character frequencies within s.
          + The longest palindrome will be the string constructed by all characters appear even time within the string and one character that has the highest occurence and that occurence must be an odd number.
          + for all characters that appear an odd number of time (say m), we can use them m-1 number of time so it'll appear an even number of time to maintain the palindromic status.
          + Lastly, since we can have one character appears odd number of time, if there is at least one character that appears odd number of time in our dictionary, add 1 to our final result.
        """
        char_freq = dict()
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        has_odd_frequency_char = False
        longest_palindrome_length = 0

        for frequencies in char_freq.values():
            if frequencies % 2 == 0:
                longest_palindrome_length += frequencies
            else:
                longest_palindrome_length += (frequencies-1)
                has_odd_frequency_char = True

        if has_odd_frequency_char:
            longest_palindrome_length += 1

        return longest_palindrome_length
