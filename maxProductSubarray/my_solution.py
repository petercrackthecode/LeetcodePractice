# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


def maxProduct(nums: List[int]) -> int:
    max_product = nums[0]
    min_product_so_far = nums[0]
    max_product_so_far = nums[0]

    for i in range(1, len(nums)):
        new_min = min(min_product_so_far *
                      nums[i], max_product_so_far * nums[i], nums[i])
        new_max = max(max_product_so_far *
                      nums[i], min_product_so_far * nums[i], nums[i])
        max_product = max(max_product, new_max)
        min_product_so_far = new_min
        max_product_so_far = new_max
    return max_product


print(maxProduct([-1, -2, -9, -6]))
