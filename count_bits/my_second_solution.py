# https://leetcode.com/problems/counting-bits/
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        ans = [0 for _ in range(n+1)]
        ans[1] = 1

        for num in range(2, n+1):
            if num % 2 == 0:
                ans[num] = ans[num // 2]
            else:
                ans[num] = ans[num - 1] + 1

        return ans
