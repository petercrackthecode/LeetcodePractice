# https://leetcode.com/problems/longest-substring-without-repeating-characters
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        + Find the longest substring where the frequencies of all characters == 1
        + Given a position i where i = [0, n-1] (n is the length of s), find all the substrings that end at position i. 
            i
        0123456
        abcdefg

        Start with all the substrings that ended at the position (n-1), then iteratively decrease it to n-2, n-3, ..., 0

        + Take the current string (s) as the substring, calculate the frequencies of every character within that substring.
            - Have a dictionary: character_freq:
                key: a character.
                value: the count of the number that character exists within our substring.
            - Have a set to save all the characters that are repeated within our substring: repeated_characters. When len(repeated_character) == 0: our substring contains only unique characters.
        + Repeat the above step for all the substrings that end at the position n-2, n-3, ..., 0.
        + Everytime we do so, adjust the count in character_freq by cutting down the last character substring[-1].
        """
        main_string_char_freq = defaultdict(int)
        repeated_characters = set()
        for char in s:
            main_string_char_freq[char] += 1
            if main_string_char_freq[char] > 1:
                repeated_characters.add(char)
        substring_end_at_pos = len(s) - 1
        ans = 0

        while substring_end_at_pos >= 0:
            start_pos = 0
            substr_char_freq = dict(main_string_char_freq)
            substr_repeated_characters = set(repeated_characters)
            while start_pos <= substring_end_at_pos:
                if len(substr_repeated_characters) == 0:
                    ans = max(ans, substring_end_at_pos - start_pos + 1)
                    break

                char_at_start = s[start_pos]
                substr_char_freq[char_at_start] -= 1
                if substr_char_freq[char_at_start] <= 1:
                    substr_repeated_characters.discard(char_at_start)

                start_pos += 1

            last_char = s[substring_end_at_pos]
            main_string_char_freq[last_char] -= 1
            if main_string_char_freq[last_char] == 1:
                repeated_characters.discard(last_char)
            substring_end_at_pos -= 1

        return ans
