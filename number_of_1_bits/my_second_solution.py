# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_rep = bin(n)[2:]

        ans = 0

        for bit in bin_rep:
            if bit == "1":
                ans += 1

        return ans
