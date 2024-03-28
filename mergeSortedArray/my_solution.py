# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
                 0 1 2 3 4 5                   0 1 2
        nums1 = [1,2,3,2,5,6], m = 3, nums2 = [2,5,6], n = 3
                     i                         j
        *** APPROACH 1 ***
        - put all elements from nums2 to the back of nums1: from index m -> len(nums1)-1 (inclusively)
        - sort nums1

        Time: O((m+n)*log(m+n))
        Space: O(1)
        """
        j: int = 0

        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j += 1

        nums1.sort()
