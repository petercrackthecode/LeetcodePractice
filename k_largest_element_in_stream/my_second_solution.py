# https://leetcode.com/problems/kth-largest-element-in-a-stream/
from heapq import heapify, heappop, heappush
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap_size_limit:int = k
        self.min_heap:List[int] = []
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.heap_size_limit or val >= self.min_heap[0]: # if the heap has fewer than k elements or val is greater than or equal to min_heap's root => push val to min_heap
            heappush(self.min_heap, val)
        if len(self.min_heap) > self.heap_size_limit: # if min_heap's size exceeds the limit, pop an element
            heappop(self.min_heap)

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)