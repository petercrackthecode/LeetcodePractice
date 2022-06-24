# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Logic:
        + Initiate the max_at_i and max_subarray_sum equal to array[0]
        + Traverse through the array from the position 1 to array_length - 1
        + Every time we move to a new index i, get the max sum subarrays that end at that index with the algorithm below:
          - max_at_i = max(max_at_i_minus_1 + array[i], array[i]): The reason we have to use max is because
          at some case the max_at_i_minus_1 is a negative number, so max_at_i_minus_1 + array[i] < array[i].
        + Compare the max_at_i to max_subarray_sum and save the max of them to max_subarray_sum:
          - max_subarray_sum = max(max_at_i, max_subarray_sum)
          The reason we do this is because the max sum subarray that ends at i doesn't guarantee itself to be the max sum subarray
          of the whole array. Since we have to pick the subarray with the largest sum, this comparison is required.
        + After the iteration, returns the max_subarray_sum. That's our answer.
        """
        ans = nums[0]
        max_till_index = nums[0]

        for index in range(1, len(nums)):
            max_till_index = max(max_till_index + nums[index], nums[index])
            ans = max(ans, max_till_index)

        return ans
