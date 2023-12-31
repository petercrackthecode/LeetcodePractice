# https://leetcode.com/problems/sliding-window-maximum/
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        brute-force solution:

        iterate i from position 0 to len(nums) - k, inclusively:
        - get the sub array of nums from position i with the length of k.
        - get the max of the subarray, then push the result to ans.
        """
        ans = []

        for i in range(len(nums) - k + 1):
            ans.append(max(nums[i:i+k]))

        return ans
