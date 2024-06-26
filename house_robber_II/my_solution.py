# https://leetcode.com/problems/house-robber-ii/
from typing import DefaultDict, List
from collections import defaultdict


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
         0  1  2  3
        [1, 2, 3, 1]

        rob 0 and 2: 1 + 3 = 4
        rob 1 and 3: 2 + 1 = 3

        rob odd-index houses
        rob even-index houses

         0  1  2  3  4  5
        [1, 2, 99, 5, 1, 20]

        rob 99 and 20 to get the max outcomes.

        At each house, we can choose to rob or not rob => 0/1 knapsack.
        One edge case: when nums has only one element (we cannot divide to the subarray cases below) => return nums[0]

        2 cases: given that n = len(nums)
        - we pick the prev_prev index => we cannot consider the last index => consider the index from 0..n-2 only
        - we don't pick the prev_prev index => our case will results from index 1..n-1
        - formula: at any index i: max_profit[i] = max(0 if i-1 < 0 else max_profit[i-1], (0 if i-2 < 0 else max_profit[i-2]) + nums[i])

        ** STEPS **
        - have a default dictionary called max_profit:DefaultDict[int, int] = defaultdict(int) to memoize the max profit until a given index i.
        - Case 1: 0..n-2:
            - loop: for i in range(n-1):
                - max_profit[i] = max(0 if i-1 < 0 else max_profit[i-1], (0 if i-2 < 0 else max_profit[i-2]) + nums[i])
            - ans = max_profit[n-2]
        - case 2: 1..n-1:
            - loop: for i in range(1, n):
                - max_profit[i] = max(0 if i-1 < 0 else max_profit[i-1], (0 if i-2 < 0 else max_profit[i-2]) + nums[i])
            - ans = max(ans, max_profit[n-1])
        - return ans

        Time: O(N)
        Space: O(1)
        """
        # Edge case: the list has only one element
        if len(nums) == 1:
            return nums[0]

        n: int = len(nums)
        prev_prev: int = 0
        prev: int = 0
        curr: int = 0

        # i-2, i-1, i, i+1
        for i in range(n - 1):
            curr = max(prev, prev_prev + nums[i])
            prev_prev = prev
            prev = curr

        # print(f'max_profit = {max_profit}')

        ans: int = curr

        prev_prev = prev = curr = 0
        for i in range(1, n):
            curr = max(prev, prev_prev + nums[i])
            prev_prev = prev
            prev = curr

        ans = max(ans, curr)

        return ans
