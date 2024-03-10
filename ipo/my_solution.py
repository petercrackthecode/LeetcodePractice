# https://leetcode.com/problems/ipo/description/
from typing import List, Tuple
from heapq import heappop, heappush
from functools import cmp_to_key


class Solution:
    def findMaximizedCapital(
        self, k: int, curr_cap: int, profits: List[int], capitals: List[int]
    ) -> int:
        """
        - Create a min-heap to store capitals
        - Identify the projects that can be invested within the range of the current capital.
        - Select the project that yields the highest profit.
        - Add the profit earned to the current capital.
        - Repeat until k projects have been selected

        """
        # min heap of (-profit, capital)
        doable_deals: List[Tuple[int, int]] = []
        # tuples stored as (profit, capital)
        # next_deals are sorted ascendingly by capital (next_deals[1])
        next_deals: List[Tuple[int, int]] = []

        for i in range(len(profits)):
            profit, capital = profits[i], capitals[i]
            if capital <= curr_cap:
                heappush(doable_deals, (-profit, capital))
            else:
                next_deals.append((profit, capital))

        next_deals.sort(key=cmp_to_key(lambda deal_1, deal_2: deal_1[1] - deal_2[1]))

        while k > 0 and len(doable_deals) > 0:

            curr_deal = heappop(doable_deals)
            profit = -curr_deal[0]
            curr_cap += profit

            while len(next_deals) > 0 and next_deals[0][1] <= curr_cap:
                ready_deal = next_deals.pop(0)
                heappush(doable_deals, (-ready_deal[0], ready_deal[1]))

            k -= 1

        return curr_cap
