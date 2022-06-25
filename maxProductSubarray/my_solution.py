# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:

def maxProduct(nums: List[int]) -> int:
    max_product = nums[0]
    min_product_so_far = nums[0]
    max_product_so_far = nums[0]

    for i in range(1, len(nums)):
        max_product = max(max_product, min_product_so_far *
                          nums[i], max_product_so_far * nums[i], nums[i])
        new_min = min(min_product_so_far *
                      nums[i], max_product_so_far * nums[i], nums[i])
        new_max = max(max_product_so_far *
                      nums[i], min_product_so_far * nums[i], nums[i])
        min_product_so_far = new_min
        max_product_so_far = new_max
    return max_product


print(maxProduct([-1, -2, -9, -6]))
