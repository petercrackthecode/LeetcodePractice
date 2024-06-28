# https://leetcode.com/problems/kth-largest-element-in-a-stream/
from heapq import heapify, heappop, heappush
from typing import List

class KthLargest:
    '''
    - have a min heap of size k, min_heap_k
    - __init__: add all elements from nums into min_heap_k
    - add (val):
        - add val to min_heap_k
        - while min_heap_k's size is greater than k: pop an element from min_heap_k
        - return min_heap_k's top

    heap_size = 3
    min_heap
    ["KthLargest",      "add", "add", "add", "add", "add"]
    [[3, [4, 5, 8, 2]], [3],    [5],  [10],  [9],   [4]]  
                         4       5      5     8      8
                8  
              /   \
            9      10
           / \                                
           
    '''
    def __init__(self, k: int, nums: List[int]):
        self.min_heap:List[int] = nums
        heapify(self.min_heap)
        self.heap_size_limit:int = k

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        while len(self.min_heap) > self.heap_size_limit:
            heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)