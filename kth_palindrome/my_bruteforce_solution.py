# https://leetcode.com/problems/find-palindrome-with-fixed-length/
from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        """
        queries = [1,2,3,4,5,90]
        intLength = 3
        [101,111,121,131,141,999]

        all palindrome numbers of length 3: 
        - 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 

        palindrome: the character on the left pointer is the same as the character on the right pointer.

        dynamic programming?
        brute-force:
        - ans = []
        - get all the numbers with n digits & check if each number is a palindrome. Save all the numbers to a list: palindromic_nums = []
        - loop: for each query in queries:
            - if query > len(palindromic_nums):
                - append -1 to ans.
            - otherwise, append palindromic_nums[query-1] to ans

        - return ans
        """
        ans = []
        palindromic_nums = []

        def is_palindrome(num: int) -> bool:
            str_num = str(num)
            left, right = 0, len(str_num) - 1

            while left < right:
                if str_num[left] != str_num[right]:
                    return False
                left += 1
                right -= 1

            return True
        num = 10 ** (intLength - 1)
        upper_bound = 10 ** intLength

        while num < upper_bound:
            if is_palindrome(num):
                palindromic_nums.append(num)
            num += 1

        for query in queries:
            ans.append(-1 if query > len(palindromic_nums)
                       else palindromic_nums[query-1])

        return ans
