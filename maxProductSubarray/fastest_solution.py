# https://leetcode.com/problems/maximum-product-subarray/

import math
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        res = math.prod(nums)
        if res > 0:
            return res
        max_till_now = min_till_now = 1
        for num in nums:
            prod_max = max_till_now * num
            prod_min = min_till_now * num

            max_till_now = max(prod_max, prod_min, num)
            min_till_now = min(prod_max, prod_min, num)
            res = max(res, max_till_now)
        return res
