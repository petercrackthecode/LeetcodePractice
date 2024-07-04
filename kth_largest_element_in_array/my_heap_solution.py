# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap:List[int] = []

        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap, num) # O(log k)
            elif num < min_heap[0]:
                continue
            else:
                heappush(min_heap, num) # O(log k)
                heappop(min_heap) # O(log k)

        # Time: O(N log k)
        # Space: O(k)

        return min_heap[0]