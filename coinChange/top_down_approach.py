# https://leetcode.com/problems/coin-change/
from collections import defaultdict
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        to reduce te repeated steps, have a dictionary called min_coins_count_with_amount (key: amount: int, value: minimum number of changes for the given amount)

        set the min_coins_count_with_amount[0] = 0 (we have 0 way to return 0 cents)

        have a helper function coinChangeHelper to get the min number of coins to draft a certain amount
        if amount exists in min_coins_count_with_amount, return min_coins_count_with_amount[amount]

        otherwise, set the min_coins_for_current_amount = amount + 1 (the max number of coins we can draft to form amount is amount => amount + 1 is a dummy value)
        for each amount, sequentially get a coin from coins, then get the remainder = amount - that_coin
        get the current minimum number of coins we can draft to get the remainder amount. call that minimum_coins_for_remainder
            if minimum_coins_for_remainder is -1, we can't form any valid combination with the said amount => skip the case
            otherwise, assign the minimum between min_coins_for_current_amount and (1 + minimum_coins_for_remainder) to min_coins_for_current_amount (plus one since we already subtract one coin from amount to get the remainder)
        if min_coins_for_current_amount > amount, that means min_coins_for_current_amount is never assigned to a valid combination => min_coins_count_with_amount[amount] = -1, else min_coins_count_with_amount[amount] = min_coins_for_current_amount
        return min_coins_count_with_amount[amount]

        within the coinChange function, return coinChangeHelper(amount)
        """
        min_coins_count_with_amount = defaultdict(int)
        min_coins_count_with_amount[0] = 0

        def coinChangeHelper(amount: int) -> int:
            nonlocal coins, min_coins_count_with_amount
            if amount in min_coins_count_with_amount:
                return min_coins_count_with_amount[amount]

            min_coins_for_current_amount = amount + 1
            for coin in coins:
                if coin > amount:
                    continue
                else:  # coin <= amount
                    remainder = amount - coin
                    min_coin_for_remainder = coinChangeHelper(remainder)
                    # with the new amount, we can't draft any valid change => skip this case
                    if min_coin_for_remainder == -1:
                        continue
                    else:
                        min_coins_for_current_amount = min(
                            min_coins_for_current_amount, 1 + min_coin_for_remainder)

            min_coins_count_with_amount[amount] = - \
                1 if min_coins_for_current_amount > amount else min_coins_for_current_amount

            return min_coins_count_with_amount[amount]

        return coinChangeHelper(amount)
