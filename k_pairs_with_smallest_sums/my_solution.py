# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
from heapq import heapify, heappop, heappush
from typing import List, Tuple

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        - have a list of pairs called ans as our going to be returned answer: ans:List[List[int]] = []
        - have a heap of 3 items called ascending_sum: (sum, index_in_nums1, index_in_nums2)
        - populate ascending_sum:
            - loop: for each number first_num at index i from 0 -> len(nums1) - 1:
                - get the first number within nums2: second_num = nums2[0]
                - add a tuple of 3 items as (first_num + second_num, i, 0) to ascending_sum
        - heapify ascending_sum (min_heap)
        - loop: while k is greater than 0:
            - pop 3 items from ascending_sum: _, nums1_idx, nums2_idx = heappop(ascending_sum)
            - add the pair (nums1[nums1_idx], nums2[nums2_idx]) to ans
            - if (nums2_idx + 1) is smaller than len(nums2):
                - first_num = nums1[nums1_idx]
                - second_num = nums2[nums2_idx+1]
                - push (first_num + second_num, nums1_idx, nums2_idx+1) to the heap: ascending_num
            - decrement k by 1
        - return ans

        N = len(nums1), M = len(nums2)

        '''
        ans:List[List[int]] = []
        # (sum, index_in_nums1, index_in_nums2)
        ascending_nums:List[Tuple[int]] = []

        # O(min(k, N))
        for i in range(min(k, len(nums1))):
            first_num:int = nums1[i]
            second_num:int = nums2[0]
            ascending_nums.append((first_num + second_num, i, 0))
        # O(NlogN)
        heapify(ascending_nums)

        # O(k)
        while k > 0:
            # O(logQ)
            _, nums1_idx, nums2_idx = heappop(ascending_nums)
            ans.append([nums1[nums1_idx], nums2[nums2_idx]])
            if nums2_idx + 1 < len(nums2):
                first_num:int = nums1[nums1_idx]
                second_num:int = nums2[nums2_idx + 1]
                # O(logQ)
                heappush(ascending_nums, (first_num + second_num, nums1_idx, nums2_idx+1))
            
            k -= 1
        # Q = min(k, N)
        # Time: O(Q) + O(QlogQ) + O(k * logQ) ~ O(klogQ)
        # Space: O(Q)
        return ans