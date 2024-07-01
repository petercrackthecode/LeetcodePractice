# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
from heapq import *
from typing import List, Tuple

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        nums = [1, 1, 1, 2, 2, 3], k = 2
        freq = {
            1: 3,
            2: 2,
            3: 1
        }

        - have a frequency counter called freq: freq:Counter[int, int] = Counter(nums)
        - have a min_heap of size k of pairs (freq, num)
        - loop: for each num, freq within freq:
            - if min_heap's size is smaller than k:
                - push the pair (freq, num) to min_heap
            - otherwise, if freq is smaller than the frequency at min_heap's root:
                - continue
            - otherwise:
                - push the pair (freq, num) to min_heap
                - pop a pair from min_heap

        - return [num for _, num in min_heap]
        '''
        freq:Counter[int, int] = Counter(nums) # O(N)
        # (freq, num)
        min_heap:List[Tuple[int, int]] = []

        for (num, freq) in freq.items(): # O(N)
            if len(min_heap) < k:
                heappush(min_heap, (freq, num)) # O(logK)
            elif freq < min_heap[0][0]:
                continue
            else:
                heappush(min_heap, (freq, num)) # O(logK)
                heappop(min_heap) # O(logK)

        return [num for _, num in min_heap] # O(N)
        # Time: O(N log K)
        # Space: O(N) + O(k) ~ O(N)
