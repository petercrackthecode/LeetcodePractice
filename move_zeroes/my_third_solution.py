# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, arr: List[int]):
        """
        [0,1,0,3,12]

        - two pointers: slow and fast
        - they will move at the same speed if arr[fast] is different from 0. otherwise, slow will stay at the position where arr[slow] = 0, and wait until arr[fast] is different from 0 to be assigned.
        - eventually, fast will scan thru the entire array and shift all the non-zeroes number to arr[slow]. At the point the first loop stop, slow either go out of range if there's no zeroes in the array (which makes the second loop not executing) or at the first position where it's supposed to be a 0 after the shift.
        - Then, if slow is still within the array's boundary, we runs the second loop from slow till the end of the array to assign all the zeroes to the end.

        + Illustration of the first loop
                      0 1 2 3 4       0 1 2 3 4       0 1 2 3 4       0 1 2 3 4       0 1 2  3 4
        arr        = [0,1,0,3,12] -> [1,1,0,3,12] -> [1,1,0,3,12] -> [1,3,0,3,12] -> [1,3,12,3,12]
        i          =  0           ->    1         ->      2       ->        3     ->           4
        index      =  0           ->    1         ->    1         ->      2       ->         3

        arr[i] != 0:  F           ->  T           ->  F           ->  T           ->  T

        # arr[i] == 0
        """
        slow = 0
        for fast in range(len(arr)):
            if arr[fast] != 0:
                # shift the non-zero number forward.
                arr[slow] = arr[fast]
                slow += 1

        for i in range(slow, len(arr)):
            arr[i] = 0
