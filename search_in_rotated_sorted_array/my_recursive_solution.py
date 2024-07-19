# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List

class Solution:
    def binary_search(self, nums: List[int], target:int, left: int, right: int) -> int:
        if left > right:
            return -1
        
        mid:int = left + (right-left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[0]: # left side is sorted
            if nums[mid] < target or nums[0] > target: # move right
                return self.binary_search(nums, target, mid+1, right)
                # left = mid + 1
            else:  # nums[mid] > target
                return self.binary_search(nums, target, left, mid-1)
                # right = mid - 1
        else: # nums[mid] < nums[0] => right side is sorted
            if nums[mid] > target or target > nums[-1]: 
                return self.binary_search(nums, target, left, mid-1)
                # right = mid - 1
            else:
                return self.binary_search(nums, target, mid+1, right)
                # left = mid + 1

    def search(self, nums: List[int], target: int) -> int:
        '''
        1 <= k <= nums.length
         0  1  2  3  4  5  6
        [0, 1, 2, 4, 5, 6, 7] -> [0, 1, 2] + [4, 5, 6, 7]
        
         l
                           r
                  m
        [4, 5, 6, 7, 0, 1, 2] | k = 3

         l
                           r
                  m
        [6, 7, 0, 1, 2, 4, 5] | k = 5 | target = 4
                      *
         0

        - if nums[mid] >= nums[0]: the side from 0 -> mid is fully sorted

        - nums[mid] == target:
            - return mid
        - figure out which side of the numsay is sorted:
            - if nums[mid] >= nums[0]: the left side is sorted
                - if nums[mid] < target: move right: left = mid + 1
                - otherwise, nums[mid] > target: # we already check if nums[mid] == target above, so no equal case
                    - if nums[0] > target: move right: left = mid + 1
                    - otherwise, nums[0] <= target: since the left side is sorted => target must be within the range of [left, mid-1]: move left: right = mid - 1
            - otherwise: the right side is sorted:
                - if nums[mid] > target: move left: right = mid - 1
                - otherwise, nums[mid] < target: # we already check if nums[mid] == target above, so no equal case
                    - if target <= nums[len(nums) - 1]: since the right side is sorted => target must be within the range of [mid+1, right]: move right: left = mid + 1
                    - otherwise, nums[len(nums) - 1] < target: since the right side is sorted, we won't find any number equals to target on the right side => target must be within the range [left, mid-1] => move left: right = mid - 1

        - return -1

        Time: O(logN)
        Space: O(1)

        at index k is the start of the second part of the nums

        - the array is semi-sorted => modified binary search
        '''

        return self.binary_search(nums, target, 0, len(nums) - 1)