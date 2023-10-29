# https://leetcode.com/problems/find-k-closest-elements/
from typing import List
from collections import deque


class Solution:
    def find_best_idx(self, arr: List[int], x: int) -> int:
        [left, right] = [0, len(arr) - 1]

        while left <= right:
            mid = left + (right-left)//2
            if mid - 1 < 0 and x <= arr[mid]:
                return mid
            elif mid + 1 >= len(arr) and arr[mid] < x:
                return mid
            elif arr[mid-1] < x and x <= arr[mid]:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            else:  # arr[mid] > x
                right = mid - 1

        return 0

    def is_closer(self, x: int, first: int, second: int) -> bool:
        first_abs = abs(first - x)
        second_abs = abs(second - x)

        return (first_abs < second_abs) or (first_abs == second_abs and first < second)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        x = 3
               0 1 2 3 4
        arr = [1,2,3,4,5]
                   x
                 l 
                   r

        [-4, -1, 3]

        - since arr is sorted, we can find an index i where we can place x in arr so that:
        arr[i-1] < x <= arr[i] (remember to check the boundary for i-1)
        => custom binary search => have a helper function called find_best_idx(self, arr: List[int], x: int) -> int: that returns the said index.

        ans = []
        i = self.find_best_idx(arr, x)
        [left, right] = [i-1, i]

        while len(ans) < k and (left >= 0 or right < len(arr)):
            if left < 0:
                ans.append(arr[right])
                right += 1
            elif right >= len(arr):
                ans.append(arr[left])
                left -= 1
            else:
                num_left = arr[left]
                num_right = arr[right]
                if self.is_closer(x, num_left, num_right):
                    ans.append(num_left)
                    left -= 1
                else:
                    ans.append(num_right)
                    right += 1

        return ans
        """
        ans = deque()
        i = self.find_best_idx(arr, x)
        [left, right] = [i-1, i]

        while len(ans) < k and (left >= 0 or right < len(arr)):
            if left < 0:
                ans.append(arr[right])
                right += 1
            elif right >= len(arr):
                ans.appendleft(arr[left])
                left -= 1
            else:
                num_left = arr[left]
                num_right = arr[right]
                if self.is_closer(x, num_left, num_right):
                    ans.appendleft(num_left)
                    left -= 1
                else:
                    ans.append(num_right)
                    right += 1

        return list(ans)
