# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        index_lookup_by_sum = {0: -1}
        max_len = 0
        total = 0

        for idx, num in enumerate(nums):
            total += num
            if total - k in index_lookup_by_sum:
                max_len = max(max_len, idx - index_lookup_by_sum[total-k])
            if total not in index_lookup_by_sum:
                index_lookup_by_sum[total] = idx
        return max_len
