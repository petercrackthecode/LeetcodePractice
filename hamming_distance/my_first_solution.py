# https://leetcode.com/problems/hamming-distance/
from collections import deque
from typing import Deque


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        Input: x = 1, y = 4
        Output: 2
        1   (0 0 0 1)
        4   (0 1 0 0)

        - have a helper function called get_binary_str(num:int) -> Deque[str] to get the binary string of an integer.
        - convert x into its binary version: x_binary:Deque[str] = get_binary_str(x)
        - convert y into its binary version: y_binary:Deque[str] = get_binary_str(y)
        - keep the length of x_binary and y_binary equal: for a shorter characters list, keep appending '0' to its beginning until two characters list share the same length
            - while len(x_binary) < len(y_binary): # x_binary is shorter than y_binary
                x_binary.append_left('0')
            - while len(y_binary) < len(x_binary):
                y_binary.append_left('0')
        - have a variable called diff_count = 0
        - loop: iterate i from 0 -> len(x_binary) inclusively:
            - if x_binary[i] is different from y_binary[i]: increment diff_count by 1
        - return diff_count

        """

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

        x_binary: Deque[str] = get_binary_str(x)
        y_binary: Deque[str] = get_binary_str(y)

        while len(x_binary) < len(y_binary):
            x_binary.appendleft("0")
        while len(y_binary) < len(x_binary):
            y_binary.appendleft("0")

        # len(x_binary) == len(y_binary)
        diff_count: int = 0

        for i in range(len(x_binary)):
            if x_binary[i] != y_binary[i]:
                diff_count += 1

        return diff_count


# x = 1
# y = 4
# ans = Solution().hammingDistance(x, y)  # expected: 2

# x = 3
# y = 1
# ans = Solution().hammingDistance(x, y)  # expected: 1
# print(f"ans = {ans}")
