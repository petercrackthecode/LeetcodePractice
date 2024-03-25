# https://leetcode.com/problems/number-of-1-bits/
from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        def decimal_to_binary_string(num: int) -> str:
            """
            - edge case: if num == 0: return '0'

            - have a list called ans to collect the binary bits. ans = []
            - loop: while num > 0:
                - get the mod of num divided by 2: remainder
                - append str(remainder) to ans.
                - assign: num = num // 2

            - return the reversed version of ans as a string: ''.join(ans[::-1])
            """
            if num == 0:
                return "0"

            ans: List[str] = []

            while num > 0:
                remainder: int = num % 2
                ans.append(str(remainder))
                num //= 2

            return "".join(ans[::-1])

        binary_rep: str = decimal_to_binary_string(n)
        # print(f"binary_rep = {binary_rep}")

        ans: int = 0

        for bit in binary_rep:
            if bit == "1":
                ans += 1

        return ans


n = 2147483645
ans = Solution().hammingWeight(n)
print(f"ans = {ans}")
