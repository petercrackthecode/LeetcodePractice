# https://leetcode.com/problems/sliding-window-maximum/
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        ans = []
        for i in range(k):
            window.append(nums[i])

        def find_insert_index(target: int) -> int:
            nonlocal window
            if len(window) == 0:
                return 0

            [left, right] = [0, len(window) - 1]

            while left <= right:
                mid = left + (right - left) // 2
                if mid == 0 and target <= window[mid]:
                    return mid
                elif mid == len(window) - 1 and target >= window[mid]:
                    return len(window)
                elif window[mid] <= target < window[mid+1]:
                    return mid + 1
                elif window[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        window.sort()
        ans.append(window[-1])
        j = 0
        for i in range(k, len(nums)):
            window.remove(nums[j])
            j += 1
            index_to_insert = find_insert_index(nums[i])
            if index_to_insert > -1:
                window.insert(index_to_insert, nums[i])
            ans.append(window[-1])

        return ans
