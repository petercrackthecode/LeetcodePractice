# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        return the minimal length of subarray whose sum is greater than or equal to target. If none, return 0
                l
                r
                0 1 2 3 4 5
        nums = [9,7,1,2,4,3]
        target = 7
        output = 1 ([7])

        sliding window approach:
        - have a variable called ans to save the length of the valid minimal subarray that we need to return. ans = len(nums) + 1
        - have left and right pointers. left initialize to 0 and right initialized to 0.
        - have a variable called sum_so_far initialized to 0 to keep track of the sum within our current window ([left, right]).
        - repeat these steps while left <= right < len(nums):
            - repeat while left is smaller than or equal to right and sum_so_far is greater than or equal to target:
                - ans = min(ans, right - left + 1)
                - subtract sum_so_far by nums[left].
                - increment left by 1.
            - if left is smaller than or equal to right and (sum_so_far < target) => extend the right window:
                - increment right by 1
                - if right is smaller than len(nums), increment sum_so_far by nums[right]


        return ans if ans is smaller than len(nums) + 1, otherwise return 0.

        Time: O(N) | N = len(nums)
        Space: O(1)
                        l
                          r
        nums = [2,3,1,2,4,3]
        target = 7
        """
        sum_so_far = nums[0]
        ans = len(nums) + 1
        left = right = 0

        while left <= right < len(nums):
            if sum_so_far >= target:  # extend left to reduce our window's size in search for a smaller valid subarray
                ans = min(ans, right - left + 1)
                sum_so_far -= nums[left]
                left += 1
            else:  # sum_so_far < target => extend right
                right += 1
                if right < len(nums):
                    sum_so_far += nums[right]

        return ans if ans < len(nums) + 1 else 0
