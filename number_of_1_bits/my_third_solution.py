# https://leetcode.com/problems/number-of-1-bits/
from collections import deque
from typing import Deque


def get_binary_str(num: int) -> Deque[str]:
    ans: Deque[str] = deque()

    """
    [1, 2, 4, 8,]
    - have a list of power of 2: called pow_2 = []
    - have a variable called curr_pow to keep track of the current power of 2: curr_pow = 1
    - loop: while curr_pow <= num: # edge case: num is 0
        - append curr_pow to pow_2
        - time curr_pow by 2
    - starting from the end of pow_2: i = len(pow_2) - 1 -> 0 (inclusively)
        - if num is smaller than pow_2[i], append '0' to ans
        - otherwise, append '1' to ans
        - num is subtracted by pow_2[i]
        - decrement i by 1.

    - if ans is empty: return ['0']
    - otherwise, return ans
    
    """
    pow_2 = []
    curr_pow = 1

    while curr_pow <= num:  # curr_pow > num
        pow_2.append(curr_pow)
        curr_pow *= 2

    for i in reversed(range(len(pow_2))):
        # print(f'num = {num}')
        if num < pow_2[i]:
            ans.append("0")
        else:
            ans.append("1")
            num -= pow_2[i]
        i -= 1

    return ans if len(ans) > 0 else deque(["0"])


class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_str = get_binary_str(n)

        ans: int = 0

        for bit in binary_str:
            if bit == "1":
                ans += 1

        return ans


n = 2147483645
ans = Solution().hammingWeight(n)
print(f"ans = {ans}")  # 1
