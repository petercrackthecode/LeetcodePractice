# https://leetcode.com/problems/counting-bits/
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        have an array from 0..n to save the number of 1s for any number i between 0..n: ans = [] (ans has the size of n+1 (0..n))
        have a variable called smaller_power_of_2 = 0
        ans[0] = 0
        ans[1] = 1
        iterate num from 2..n:
        if num is a power of 2 (math.log2(num) == math.floor(math.log2(num))), then ans[num] = 1, and we save num to smaller_power_of_2
        otherwise, ans[num] is the sum of 1 + ans[num - smaller_power_of_2]

        return ans
        """
        if n == 0:
            return [0]

        ans = [0 for _ in range(n+1)]
        ans[1] = 1
        smaller_power_of_2 = 0

        for num in range(2, n+1):
            if math.log2(num) == math.floor(math.log2(num)):
                ans[num] = 1
                smaller_power_of_2 = num
            else:
                ans[num] = 1 + ans[num - smaller_power_of_2]

        return ans
