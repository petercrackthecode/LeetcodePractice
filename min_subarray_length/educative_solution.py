# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    # Initialize window_size with positive infinity
    window_size = len(nums) + 1
    # Initialize start and sum with 0
    start = 0
    sum = 0
    # Iterate over the input array
    for end in range(len(nums)):
        sum += nums[end]
        # Remove elements from the start of the window while sum is greater than target
        while sum >= target:
            # Find size of current window
            curr_subarr_size = (end + 1) - start
            window_size = min(window_size, curr_subarr_size)
            # Remove element frmo the start of the window
            sum -= nums[start]
            start += 1

    return window_size if window_size < len(nums) + 1 else 0
