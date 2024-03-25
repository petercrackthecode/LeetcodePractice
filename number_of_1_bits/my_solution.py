# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_representation: str = bin(n)[2:]
        print(f"binary_representation = {binary_representation}")

        ans: int = 0

        for bit in binary_representation:
            if bit == "1":
                ans += 1

        return ans


n = 2147483645
ans = Solution().hammingWeight(n)
print(f"ans = {ans}")
