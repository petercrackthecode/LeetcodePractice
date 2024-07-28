# https://leetcode.com/problems/find-k-closest-elements/
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        - arr is sorted.

                     x
        arr = [1, 2, 3, 4, 5]
        k   = 4
        x   = 3

        [1, 2, 5, 8, 15] | x = 10
        [1, 2, 10, 10, 10, 11]
                        i

        - given the list arr, find the index i where arr[i] <= x < arr[i+1] (if exists) (modified binary search)
        - have 2 pointers left = i, right = i + 1
        - loop: while k > 0 and (left >= 0 or right < len(nums)):
            - if right >= len(nums):
                - decrement left by 1
            - otherwise, if left < 0:
                - increment right by 1.
            - otherwise, both left and right is in bound:
                - if is_closer_to_x(arr[left], arr[right]) is true: arr[left] is closer to x than arr[right]:
                    - decrement left by 1
                - otherwise:
                    - increment right by 1
            - decrement k by 1

        - return arr[left+1:right]
        """

        def find_closest_idx(x: int) -> int:
            nonlocal arr
            left, right = 0, len(arr) - 1

            while left <= right:
                mid: int = left + (right - left) // 2
                right_bound: int = float("inf") if mid + 1 >= len(arr) else arr[mid + 1]
                if arr[mid] <= x < right_bound:
                    return mid
                elif right_bound <= x:
                    left = mid + 1
                else:
                    right = mid - 1

            # x is smaller than all numbers in arr
            return 0

        def is_closer_to_x(a: int, b: int) -> bool:
            nonlocal x
            a_dist: int = abs(a - x)
            b_dist: int = abs(b - x)

            return a_dist < b_dist if a_dist != b_dist else a < b

        closest_idx: int = find_closest_idx(x)
        left, right = closest_idx, closest_idx + 1

        while k > 0 and (left >= 0 or right < len(arr)):
            if right >= len(arr):
                left -= 1
            elif left < 0:
                right += 1
            else:
                if is_closer_to_x(arr[left], arr[right]):
                    left -= 1
                else:
                    right += 1

            k -= 1

        return arr[left + 1 : right]
