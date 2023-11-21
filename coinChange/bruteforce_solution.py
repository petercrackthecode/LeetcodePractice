# https://leetcode.com/problems/coin-change/description/
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        initialize ans to a dummy value: amount + 1 
        (the maximum amount of coins we can return is amount (amount = 1 cent * amount_time))

        edge case: if the amount is 0, return 0 (we have no way to return 0 from our coin)
        inorderly select a coin from coins:
            if the current coin is greater than amount, terminate the loop
            if the current coin is equal to the amount, assign ans to the minimum between ans and coins_count + 1
            if the current coin is smaller than the amount, get the remainder equals to amount subtracted by the current coin, the call the coinChangeHelper function with the new amount
            and new coins_count (coins_count + 1)
        keep running the loop above until we've reached the end of all coins.

        return -1 if ans > amount else ans
        """

        if amount == 0:
            return 0

        ans = amount + 1

        def coinChangeHelper(amount: int, coins_count: int):
            nonlocal coins, ans
            for coin in coins:
                if coin >= amount:
                    if coin == amount:
                        ans = min(ans, coins_count + 1)
                    break
                else:  # coin < amount
                    remainder = amount - coin
                    coinChangeHelper(remainder, coins_count + 1)

        coinChangeHelper(amount, 0)
        return -1 if ans > amount else ans
