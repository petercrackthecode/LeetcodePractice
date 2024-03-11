# https://leetcode.com/problems/ipo/description/
from heapq import heappop, heappush
from typing import List, Tuple


def maximum_capital(c: int, k: int, capitals: List[int], profits: List[int]) -> int:
    current_capital: int = c
    capitals_min_heap: List[Tuple[int, int]] = []
    profits_max_heap: List[int] = []

    for x in range(0, len(capitals)):
        heappush(capitals_min_heap, (capitals[x], profits[x]))

    for _ in range(k):
        while capitals_min_heap and capitals_min_heap[0][0] <= current_capital:
            c, p = heappop(capitals_min_heap)
            heappush(profits_max_heap, -p)

        if not profits_max_heap:
            break

        j = -heappop(profits_max_heap)
        current_capital += j

    return current_capital
