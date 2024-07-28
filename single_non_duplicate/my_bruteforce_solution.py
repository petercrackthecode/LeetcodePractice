# https://leetcode.com/problems/single-element-in-a-sorted-array/
from typing import List


class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        """
        Brute-force solution:
                0  1  2  3  4  5  6  7  8  9
        arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
                      *
        ans  = 2

        arr = [1, 1, 2, 2, 3, 3, 4, 4, 8, 8]
                                     *

        arr = [1, 1, 2]
                      i

        arr = [1, 2, 2]
                i

        arr = [1]
                i

        - index i:
            - if i - 1 exists:
                - if arr[i-1] < arr[i]: arr[i+1] must exist and arr[i+1] == arr[i] for the number at index i to appear twice.
                - otherwise, arr[i-1] must be equal to arr[i] for the number at index i to appear twice.
            - if i- 1 doesn't exist (i == 0):
                - arr[i+1] must exist and be equal to arr[i] for the number at index i to appear twice.


        - arr is sorted
        - every element appears twice, except one element appear once.
        """
        ans: int = arr[0]

        for i in range(len(arr)):
            if i - 1 >= 0:
                if arr[i - 1] < arr[i]:
                    if not (i + 1 < len(arr) and arr[i + 1] == arr[i]):
                        ans = arr[i]
                        break
                else:  # arr[i-1] == arr[i] since arr is sorted
                    pass
            else:  # i-1 doesn't exist
                if not (i + 1 < len(arr) and arr[i] == arr[i + 1]):
                    ans = arr[i]
                    break

        return ans
        # Time: O(N)
        # Space: O(1)
