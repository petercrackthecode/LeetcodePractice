# https://leetcode.com/problems/single-element-in-a-sorted-array/
from typing import List


class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        """
        - left_bound = arr[m-1] if m-1 >= 0 else float('-inf')
        - right_bound = arr[m+1] if m+1 < len(arr) else float('inf')

        - if left_bound < arr[mid] < right_bound: return mid
        - m + 1 exists:
            - if arr[mid+1] == arr[mid]
                if (r-m) is an odd number: - move left
                else: move right
            - otherwise, arr[mid+1] is different from arr[mid]:
                if (r-m) is an even number: - move left
                otherwise: move right
        - otherwise, m+1 doesn't exist and m is not the single-element index: move left

        ans = 2

        arr = [1, 1, 2]
                     l
                     m
                     r

               0  1  2
        arr = [1, 2, 2]
               l
               m
               r

        arr = [1]
               l
               m
               r

        - arr is sorted
        - every element appears twice, except one element appear once.
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid: int = left + (right - left) // 2
            left_bound = arr[mid - 1] if mid - 1 >= 0 else float("-inf")
            right_bound = arr[mid + 1] if mid + 1 < len(arr) else float("inf")

            if left_bound < arr[mid] < right_bound:
                return arr[mid]
            elif mid + 1 < len(arr):
                if arr[mid + 1] == arr[mid]:
                    if (len(arr) - 1 - mid) % 2 == 1:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:  # arr[mid+1] != arr[mid]
                    if (len(arr) - 1 - mid) % 2 == 0:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:  # mid + 1 doesn't exist and mid is not the index of the single element we're looking for => move left
                right = mid - 1

        return arr[0]
