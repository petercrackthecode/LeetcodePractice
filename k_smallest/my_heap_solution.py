# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        matrix = [
            [1, 5, 9 ],
            [10,11,13],
            [12,13,15]
        ]
        n = 3 => n*n = 9
        k = 8

         0 1 2 3  4  5  6  7  8
        [1,5,9,10,11,12,13,13,15]

        max_heap = []

        return the (n*n-k+1)_th element from the back of the list. popping from the back of an array only takes O(1)
        - have a max_heap called max_heap to save the greatest number. max_heap = []
        - loop thru every array at row i in matrix:
            - get the last element: last_elem = matrix[i][-1]
            - push the pair of (-last_elem, row, n-1) into max_heap.
        - have a variable called order_from_back = (n*n-k+1)
        - loop while order_from_back > 0:
            - decrement order_from_back by 1
            - pop a pair (neg_ele, row, last_index) from max_heap
            - if order_from_back is 0: return -neg_elem
            - if last_index > 0:
                - new_index = last_index - 1
                - new_elem = -matrix[row][new_index]
                - push (new_elem, row, new_index) to our heap.
        """
        max_heap = []
        n = len(matrix)

        order_from_back = n * n - k + 1
        for row in range(n):
            last_elem = matrix[row][n - 1]
            heappush(max_heap, (-last_elem, row, n - 1))

        while order_from_back > 0:
            order_from_back -= 1
            (neg_ele, row, last_valid_index) = heappop(max_heap)
            if order_from_back == 0:
                return -neg_ele

            if last_valid_index > 0:
                new_index = last_valid_index - 1
                new_elem = -matrix[row][new_index]
                heappush(max_heap, (new_elem, row, new_index))

        # dummy return
        return matrix[0][0]
