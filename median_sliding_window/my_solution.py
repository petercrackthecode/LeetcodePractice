# https://leetcode.com/problems/sliding-window-median/
from typing import List
from heapq import heappush, heappop


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        - Declare a min-heap and a max-heap to store the elements of the sliding window.
        - Push k elements onto the max-heap and transfer k/2 numbers (the higher numbers) to the min-heap.

        - Compute the median of the window elements. If the window size is even, it's the mean of the top of the two heaps.
        If it's odd, it's the top of the max-heap.
        - Move the window forward and rebalance the heaps.
        - If the incoming number is less than the top of the max-heap, push it onto the max-heap, else, push it onto
        the min-heap.
        - If the outgoing number is at the top of either of the heaps, remove it from that heap.
        - Repeat the steps to calculate the median, add the incoming number, rebalance the heaps, and remove the outgoing
        number from the heaps.
        """
        # the first half of the list. Remember to negate each number going in/out.
        max_heap: List[int] = []
        # the second half of the list
        min_heap: List[int] = []

        i: int = 0

        while i < k:
            heappush(max_heap, -nums[i])
            i += 1

        for _ in range(k // 2):
            root = -heappop(max_heap)
            heappush(min_heap, root)
