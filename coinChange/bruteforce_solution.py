# https://leetcode.com/problems/coin-change/description/
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        given an amount, return the minimum number of coins we can create whose sum is equal to that amount.
        if that amount of money cannot be made up from any combination of the coins, return -1.
        """
        if amount == 0:
            return 0

        coins.sort()

        min_amount: float = float("inf")

        for coin in coins:
            if coin > amount:
                break
            # coin <= amount
            remainder: int = amount - coin
            number_of_coins = 1 + self.coinChange(coins, remainder)
            min_amount = min(min_amount, number_of_coins)

        return int(min_amount) if min_amount != float("inf") else -1
