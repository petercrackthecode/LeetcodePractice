class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s: str) -> bool:
            [left, right] = [0, len(s) - 1]

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        [left, right] = [0, len(s) - 1]
        did_remove_char = False

        while left < right:
            if s[left] != s[right]:

                if did_remove_char:
                    return False
                did_remove_char = True

                if s[left + 1] == s[right] or s[left] == s[right - 1]:
                    return is_palindrome(s[left+1: right+1]) or is_palindrome(s[left: right])
                else:
                    return False
            else:
                left += 1
                right -= 1

        return True
