# https://leetcode.com/problems/find-median-from-data-stream/description/
from heapq import heappush, heappop
from typing import List


class MedianFinder:
    """
    Constraints:
    - -10^5 <= num <= 10^5
    - There will be at least one element in the data structure before calling findMedian.
    - At most 5 * 10^4 calls will be made to addNum and findMedian.

    Steps:
    1. Split up incoming numbers into two lists- small and large. Those that are smaller than the current middle element are small, and those that are larger than it are large.
    2. Maintain these lists as heaps so that the root of the small heap is the largest element in it and the root of the large heap is the smallest element in it.
    3. If the size of the large heap is greater than the size of the small heap or, if the size of the small heap is greater than the size of the large heap + 1, rebalance the heaps.
    4. If the number of elements is even, the median is the mean of the root of the two heaps. Else, it's the root of the small heap.
    """

    def __init__(self):
        # self.max_heap is the first half of the list
        self.max_heap: List[int] = []
        # self.min_heap is the second half of the list
        self.min_heap: List[int] = []

    # add num to our MedianFinder
    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0 and len(self.max_heap) == 0:
            heappush(self.max_heap, -num)
            return

        max_heap_root: int = -self.max_heap[0]

        if num > max_heap_root:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)

        if len(self.max_heap) - len(self.min_heap) >= 2:
            popped = -heappop(self.max_heap)
            heappush(self.min_heap, popped)
        elif len(self.min_heap) - len(self.max_heap) >= 2:
            popped = heappop(self.min_heap)
            heappush(self.max_heap, -popped)

    # returns the median of our datastructure.
    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            min_heap_root: int = self.min_heap[0]
            max_heap_root: int = -self.max_heap[0]
            return (min_heap_root + max_heap_root) / 2
        else:  # one heap has one element more than the other
            return (
                self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else -self.max_heap[0]
            )
