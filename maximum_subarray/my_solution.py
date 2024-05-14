# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        ** Explanation:
        - We can divide the problem into:
        1. Find all the subarrays that end at index i=0
        2. Get the max_sum of all subarrays that end at index i=0
        3. Repeat the same steps for all subarrays that end at index i=1..len(nums)-1

        - The step of finding all sub arrays that end at index i=0 and finding the max_sum of all subarrays ending at index i=0 is the most expensive step. If we can convert that to O(1), we will significantly increase our speed.
        - We realize that a sub_array that ends at index i will depend on the subarray that ends at index i-1. Say that the max_till_index[i] represents the sum of the subarray that ends at index i who has the biggest sum among its peer, max_till_index[i] will depend on the result of max_till_index[i-1]
        - Next, we see that to calculate max_till_index[i], we have 2 possible solutions:
            - max_till_index[i] = nums[i]
            - max_till_index[i] = max_till_index[i-1] + nums[i]
        - we get the max of those two solution since there is a case where nums[i] > 0 but max_till_index[i-1] < 0, then (max_till_index[i-1] + nums[i]) > nums[i] (otherwise, max_till_index[i-1] + nums[i] typically > nums[i]).
        => we have the formula: max_till_index[i] = max(max_till_index[i-1] + nums[i], nums[i])
        - Base case: max_till_index[0] = nums[0] since there's only one subarray that ends at index 0: [nums[0]]

        - We then realize that we don't always need to save the entire max_till_index array since we only need the most recent max_till_index value
        => we compare & update max_till_index every loop, and each time compare the new max_till_index value with our ans to get the globally biggest sum of all subarrays

        Time: O(N)
        Space: O(1)
        """
        max_till_index: int = nums[0]
        ans: int = nums[0]

        for i in range(1, len(nums)):
            max_till_index = max(max_till_index + nums[i], nums[i])
            ans = max(max_till_index, ans)

        return ans
