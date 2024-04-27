# https://leetcode.com/problems/coin-change/
from typing import List, Dict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        compute the minimum number of coins to calculate the change ranging from 0 -> amount (inclusive)
        amount = 7, coins = [2, 3, 5]
        min_coins[0] = 0
        min_coins[1] = -1
        min_coins[2] = 1
        min_coins[3] = min(1 + min_coins[1], 1 + min_coins[0])

        have a dictionary called min_coins (key: amount: int, value: min number of coins to get the amount: int). initialize min_coins[0] = 0 (there is zero way to return 0 cents)
        for a curr_amount within the range [0, amount]:
            have a variable called min_coins_for_curr_amount initialized = (curr_amount + 1) (this is an invalid value since for any curr_amount, the max number of coins to draft it is curr_amount * 1 cent)
            iteratively subtract the current amount with a coin in coins to get the remainder. check if the remainder >= 0:
            - no: skip to the next iteration.
            - yes:
                check the ways to form the remainder (min_coins[remainder]). check if min_coins[remainder] == -1:
                    yes: skip this iteration.
                    no: min_coins_for_curr_amount = min(min_coins_for_curr_amount, 1 + min_coins[remainder])
            if the min_coins_for_curr_amount != curr_amount + 1, we have at least 1 valid way to draft curr_amount from our coins => min_coins[curr_amount] = min_coins_for_curr_amount. otherwise, min_coins[curr_amount] = -1

        return min_coins[amount]
        """
        min_coins: Dict[int, int] = dict()
        min_coins[0] = 0

        for curr_amount in range(1, amount + 1):
            min_coins_for_curr_amount: int = curr_amount + 1
            for coin in coins:
                remainder: int = curr_amount - coin
                if remainder < 0:
                    continue
                if min_coins[remainder] != -1:
                    min_coins_for_curr_amount = min(
                        min_coins_for_curr_amount, 1 + min_coins[remainder]
                    )

            min_coins[curr_amount] = (
                min_coins_for_curr_amount
                if min_coins_for_curr_amount != curr_amount + 1
                else -1
            )

        return min_coins[amount]
