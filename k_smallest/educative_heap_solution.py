# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
from typing import List
from heapq import heappop, heappush


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        - Push the first element of each list in the min-heap.

        - Remove the top (root) of the min-heap.
        - If the popped element has the next element in its list, push the next element in the min-heap.
        - If k elements has been removed from the heap, return the last popped element.
        """
        n = len(matrix)
        popped_left: int = k
        min_heap: List[int] = []

        for i in range(n):
            # pair: (elem, row, col)
            heappush(min_heap, (matrix[i][0], i, 0))

        next_elem: Optional[int] = None

        while popped_left > 0 and bool(min_heap):
            (elem, row, col) = heappop(min_heap)
            next_elem = elem
            if col < n - 1:
                new_elem = matrix[row][col + 1]
                heappush(min_heap, (new_elem, row, col + 1))
            popped_left -= 1

        return next_elem if next_elem != None else 10**9
