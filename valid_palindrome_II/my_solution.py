# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Brute force: check if the substr is a palindrome already. If not, repeatedly deleting the characters at position 0 -> len(s) - 1. Each time we remove a character, we have a new substr, and check if that new substr is a palindrome.

        two pointers to check palindrome: left and right ptr (left = 0, right = len(s) - 1) keep moving the left pointer forward (left += 1) and the right pointer backward (right -= 1) while s[left] is equal to s[right]. Return true if left >= right, otherwise, return false.

        modified two pointers: Whenever we notice two characters at left and right are different, we see if we delete the character at left and take the substr s[left+1:right+1], is that subsubstr a palindrome. Similarly, we see if we delete the character at right and take the substr s[left:right], is that subsubstr a palindrome. Return true if one of them is true.
        If two characters at left and right are the same, increment left by one & decrement right by 1.
        Keep repeating the above step while left < right
        """
        def is_palindrome(substr: str):
            [left, right] = [0, len(substr) - 1]
            while left < right:
                if substr[left] != substr[right]:
                    return False
                left += 1
                right -= 1
            return True

        [start, end] = [0, len(s) - 1]
        while start < end:
            if s[start] != s[end]:
                return is_palindrome(s[start+1:end+1]) or is_palindrome(s[start:end])
            start += 1
            end -= 1

        return True
