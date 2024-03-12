# https://leetcode.com/problems/find-median-from-data-stream/description/
from heapq import heappop, heappush
from typing import List


class MedianOfStream:
    def __init__(self):
        self.max_heap_for_smallnum: List[int] = []
        self.min_heap_for_largenum: List[int] = []

    def insert_num(self, num: int) -> None:
        if not self.max_heap_for_smallnum or -self.max_heap_for_smallnum[0] >= num:
            heappush(self.max_heap_for_smallnum, -num)
        else:
            heappush(self.min_heap_for_largenum, num)

        if len(self.max_heap_for_smallnum) > len(self.min_heap_for_largenum) + 1:
            heappush(self.min_heap_for_largenum, -heappop(self.max_heap_for_smallnum))
        elif len(self.max_heap_for_smallnum) < len(self.min_heap_for_largenum):
            heappush(self.max_heap_for_smallnum, -heappop(self.min_heap_for_largenum))

    def find_median(self) -> float:
        if len(self.max_heap_for_smallnum) == len(self.min_heap_for_largenum):

            # we have an even number of elements, take the average of middle two elements
            return (-self.max_heap_for_smallnum[0] + self.min_heap_for_largenum[0]) / 2
        return float(-self.max_heap_for_smallnum[0])
