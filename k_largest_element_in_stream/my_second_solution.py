# https://leetcode.com/problems/kth-largest-element-in-a-stream/
from heapq import heapify, heappop, heappush
from typing import List

class KthLargest:
    '''
    - Initialize a min-heap in the constructor to store the elements. Iterate through the elements in nums and call the
    add function for each element.
    - In the add function, if the size of the heap is less than k, push the number into the heap. Otherwise, if the incoming
    value is greater than the smallest element (top of the heap), perform a pop operation to remove the smallest element,
    and then push the new value into the heap.
    - After adding all the numbers, the kth largest element can be found at the root of the heap.
    '''
    def __init__(self, k: int, nums: List[int]): # Time: O(nlogk)
        self.heap_size_limit:int = k
        self.min_heap:List[int] = []
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int: # Time: O(logk)
        if len(self.min_heap) < self.heap_size_limit or val >= self.min_heap[0]: # if the heap has fewer than k elements or val is greater than or equal to min_heap's root => push val to min_heap
            heappush(self.min_heap, val)
        if len(self.min_heap) > self.heap_size_limit: # if min_heap's size exceeds the limit, pop an element
            heappop(self.min_heap)

        return self.min_heap[0]

    # Overall space: O(k)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)