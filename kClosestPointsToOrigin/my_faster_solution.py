# https://leetcode.com/problems/k-closest-points-to-origin/
from typing import List, Tuple
from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        points = [[1,3], [-2,2]], k = 1
        ans = [[-2, 2]]

        dist([1, 3]) = ((1 - 0)^2 + (3 - 0)^2) ** 1/2 = 10 ** 1/2
        dist([-2, 2]) = ((-2 - 0)^2 + (2 - 0)^2) ** 1/2 = 8 ** 1/2

        k closest points to (0, 0)

        use a max_heap of tuples of (dist, x, y) of size k
        when we add a new val (new_dist, new_x, new_y) to the heap: max_heap's root is the node with the longest distance to O(0,0) among the k nodes
        - if max_heap's length is smaller than k:
            - push (-new_dist, new_x, new_y) to max_heap
        - otherwise, if new_dist is greater than the distance at max_heap's root:
            - continue
        - otherwise:
            - push (-new_dist, new_x, new_y) to max_heap
            - pop an element from max_heap

        - return [[x, y] for _, x, y in max_heap] 
        '''
        # (neg_dist, x, y)
        max_heap:List[Tuple[float, int, int]] = []

        for new_x, new_y in points: # O(N)
            new_dist:float = (new_x ** 2 + new_y ** 2) ** 1/2
            if len(max_heap) < k:
                heappush(max_heap, (-new_dist, new_x, new_y)) # O(logK)
            # below: max_heap's length >= k >= 1
            elif new_dist > -max_heap[0][0]:
                continue
            else:
                heappush(max_heap, (-new_dist, new_x, new_y)) # O(logK)
                heappop(max_heap) # O(logK)

        return [[x, y] for _, x, y in max_heap] # O(N)

        # Time: O(N log K)
        # Space: O(K)