# https://leetcode.com/problems/longest-substring-without-repeating-characters
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        * General logic: sliding window problem.
        + Have 2 variables: substr_start & substr_end, which each respectively represents the start & the end position of
        the substr we're assessing.
        + Iterate through every single character in s. Each time we see a new character at the position i:
        - If a character is unique within the substr, compare the max between the longest_substr_length & 
        the longest_substr_so_far (substr_end - substr_start + 1), then assign that value to longest_substr_length
        - Else: we have a new character that break the uniqueness of our substr: => we have to shrink our substr to keep it valid.
            start eliminating the character at substr_start, then increment the substr_start by 1 until our substr is
            unique again (characters_frequencies[character] <= 1)
          We don't have to worry about the comparison between longest_substr_length & longest_substr_so_far in this case
          because as we're shrinking our substr, the new substr we've just obtained will have the length 
          smaller than or equal to the previous valid substr (unique characters) we have saved (by comparing between 
          longest_substr_length & longest_substr_so_far)
        - In the end, there can be a case we we shrink our substr (the Else case), then we hit the end of s without checking
          for the longest_substr_length. Hence, we reduce substr_end by 1 (since substr_end == len(s) beforehand, which errs
          our calculation), then check for the longest_substr_length one more time: 
            - longest_substr_length = max(longest_substr_length, substr_end - substr_start + 1)
        - Return the longest_substr_length as our answer.
        """
        characters_frequencies = Counter()
        longest_substr_length = 0
        substr_start = 0
        substr_end = 0

        while substr_end < len(s) and substr_start <= substr_end:
            character = s[substr_end]
            characters_frequencies[character] += 1
            if characters_frequencies[character] <= 1:
                longest_substr_length = max(
                    longest_substr_length, substr_end - substr_start + 1)
            # characters_frequencies[character] >= 1: we have at least one duplicate.
            else:
                while substr_start <= substr_end and characters_frequencies[character] > 1:
                    characters_frequencies[s[substr_start]] -= 1
                    substr_start += 1

            substr_end += 1
        # reduce the substr_end by 1 to get the right calculation at line #48 since substr_end == len(s) now.
        substr_end -= 1
        longest_substr_length = max(
            longest_substr_length, substr_end - substr_start + 1)

        return longest_substr_length


s = "abcabcbb"
result = Solution().lengthOfLongestSubstring(s)
print('result = ', result)
