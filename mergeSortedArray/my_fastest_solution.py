# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        - place k at n
        - i = 0
        - j = 0

        - loop: while k is smaller than m+n and j is smaller than n:
            - next_num = 0
            - if nums1[k] is smaller than nums2[j]:
                - assign: next_num = nums1[k]
                - increment k by 1
            - otherwise:
                - next_num = nums2[j]
                - increment j by 1
            - assign: nums1[i] = next_num
            - increment i by 1

        - add the remaining numbers in nums1 (if there any):
            - loop: while k < m+n and i < m+n:
                - assign: nums1[i] = nums1[k]
                - increment both i and k by 1

        - add the remaining numbers in num2 (if there any):
            - loop: while j < n and i < m+n:
                - assign: nums1[i] = nums2[j]
                - increment both i and j by 1

        Time: O(N)
        Space: O(1)

        We don't need to move the numbers to the back.
        """
        k = m + n - 1
        # nums1 pointer
        i = m - 1
        # nums2 pointer
        j = n - 1

        while 0 <= i and 0 <= j:
            # since we're traversing from the back of both two list, we use the greater than condition
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        while 0 <= i and 0 <= k:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1

        while 0 <= j and 0 <= k:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
