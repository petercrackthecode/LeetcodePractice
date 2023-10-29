# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
                 8
               [2,3,1,2]
        nums = [2,3,1,2,4,3]
        target = 7
        output = 2
        subarray [4, 3]

        - have 2 ptrs: left and right
        - sliding windows: have a curr_sum variable to keep track of the sum of the current subarray within our range.
        - keep extending to the right if our curr_sum < target. Once curr_sum > target, truncate from the left.
        - if our curr_sum is greater than or equal to target, compare the current length of our subarray (right - left + 1) to ans, and assign the min of them to ans.


        [left, right] = [0, 0]
        ans = len(nums) + 1
        curr_sum = nums[left]

        while right < len(nums) and left < len(nums):
            if curr_sum >= target:
                subarray_length = right - left + 1
                ans = min(ans, subarray_length)
                curr_sum -= nums[left]
                left += 1
            else: # curr_sum < target
                right += 1
                if right < len(nums):
                    curr_sum += nums[right]

        return 0 if ans == len(nums) + 1 else ans
        """
        [left, right] = [0, 0]
        ans = len(nums) + 1
        curr_sum = nums[left]

        while right < len(nums) and left < len(nums):
            if curr_sum >= target:
                subarray_length = right - left + 1
                ans = min(ans, subarray_length)
                curr_sum -= nums[left]
                left += 1
            else:  # curr_sum < target
                right += 1
                if right < len(nums):
                    curr_sum += nums[right]

        return 0 if ans == len(nums) + 1 else ans
