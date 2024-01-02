# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
from collections import defaultdict
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """
        - Compute the prefix sum array where psum[i] is the sum of all the elements from 0 to i.
        - At each index i, the sum of the prefix is psum[i], so we are searching for the index x where psum[x] = psum[i] - k. The subarray [x+1, i] will be of sum k.
        - Use a hashmap to get the index x efficiently or to determine that it does not exist.
        """
        prefix_sum = []
        sum_so_far = 0
        sum_to_first_index = defaultdict(int)
        ans = 0

        for i, num in enumerate(nums):
            sum_so_far += num
            prefix_sum.append(sum_so_far)
            if sum_so_far not in sum_to_first_index:
                sum_to_first_index[sum_so_far] = i

        for i, p_sum in enumerate(prefix_sum):
            remainder = p_sum - k
            if remainder == 0:
                ans = max(ans, i + 1)
            elif remainder in sum_to_first_index:
                start = sum_to_first_index[remainder]
                ans = max(ans, i - start)

        return ans
