from typing import List
import heapq


def array_to_max_heap(stones: List[int]) -> List[int]:
    ans = [-stone for stone in stones]
    heapq.heapify(ans)
    return ans


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Use a max_heap
        + add all stones to a max heap.
        + while len(max_heap) > 1:
            heaviest_stone = -heapq.heappop(max_heap)
            second_heaviest_stone = -heapq.heappop(max_heap)
            if heaviest_stone > second_heaviest_stone:
                new_stone = heaviest_stone - second_heaviest_stone
                heapq.heappush(-new_stone)

        """
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones[0]

        max_heap = array_to_max_heap(stones)
        while len(max_heap) > 1:
            heaviest_stone = -heapq.heappop(max_heap)
            second_heaviest_stone = -heapq.heappop(max_heap)
            if heaviest_stone > second_heaviest_stone:
                new_stone = heaviest_stone - second_heaviest_stone
                heapq.heappush(max_heap, -new_stone)

        return (-heapq.heappop(max_heap) if len(max_heap) == 1 else 0)
