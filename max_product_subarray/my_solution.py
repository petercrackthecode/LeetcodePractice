# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        ** LOGIC **
        - Divide the problem into 3 cases:
        1. Find all the subarrays that end at index i=0
        2. Find the maximum product of all arrays that end at index i=0
        3. Repeat the same steps above for indices from 1 to len(nums)-1

        - In case nums[i] > 0: max_product_till_index[i] = nums[i] * max_product_till_index[i-1]
        - In case nums[i] < 0: nums[i] * max_product_till[i-1] < nums[i] * min_product_till[i-1] => we gotta keep track of both the max_product and the min_product till index i-1.
        - The case nums[i] == 0 is a special case where it will rot all of our next max_product_till_index and min_product_till_index (since 0 times any number is 0). This will falsifies our algo (for example, if our list is [0, 2, 4], our algo will return 0 but it should be 2*4 = 8).
        => Instead of only comparing (nums[i] * min_product_till[i-1]) and (nums[i] * max_product_till[i-1]), we should also compare it with nums[i] (in case nums[i-1] is 0 which makes both min_product_till[i-1] and max_product_till[i-1] equal 0).
        - So, at each loop, we have our formula:
            - temp_max = max_product_till[i-1]
            - max_product_till[i] = max(min_product_till[i-1] * nums[i], temp_max * nums[i], nums[i])
            - min_product_till[i] = min(min_product_till[i-1] * nums[i], temp_max * nums[i], nums[i])
            - keep track of the global max product at each step: ans = max(ans, max_product_till[i])
        """
        max_prod_till_index: int = nums[0]
        min_prod_till_index: int = nums[0]

        ans: int = nums[0]

        for i in range(1, len(nums)):
            min_prod_till_index, max_prod_till_index = (
                min(
                    min_prod_till_index * nums[i],
                    max_prod_till_index * nums[i],
                    nums[i],
                ),
                max(
                    min_prod_till_index * nums[i],
                    max_prod_till_index * nums[i],
                    nums[i],
                ),
            )
            ans = max(ans, max_prod_till_index)

        return ans
