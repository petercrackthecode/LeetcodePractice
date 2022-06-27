# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [char.lower() for char in s if char.isalnum()]
        return s_list == s_list[::-1]
