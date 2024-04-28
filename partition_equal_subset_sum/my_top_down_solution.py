# https://leetcode.com/problems/partition-equal-subset-sum/
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        - get the total sum of every elements in nums.
        - get the half total sum: half_sum:float = sum(nums) / 2
        - if half_sum is not an integer (half_sum != int(half_sum)): return False immediately.
        - otherwise, convert the problem back to can_get_sum_in_nums(half_sum) -> bool.

        """

        # nums = [1,5,11,5]
        half_sum: float = sum(nums) / 2
        if half_sum != int(half_sum):
            return False

        target: int = int(half_sum)
        nums.sort(reverse=True)

        """
        -1: uninitialized.
         0: False
         1: True
        """
        dp: List[List[int]] = [
            [-1 for _ in range(target + 1)] for __ in range(len(nums) + 1)
        ]

        def can_sum_to_target(target: int, items_count: int) -> bool:
            nonlocal nums
            if target == 0:
                dp[items_count][target] = 1
            elif items_count == 0:  # target > 0
                dp[items_count][target] = 0
            elif (
                dp[items_count][target] == -1
            ):  # no pre-calculation found => need to calculate this value
                curr_item = nums[items_count - 1]
                if curr_item > target:
                    # since the list is sorted descending, we cannot move further toward the left since we'll only see bigger number
                    dp[items_count][target] = 0
                else:  # curr_item <= target
                    dp[items_count][target] = can_sum_to_target(
                        target - curr_item, items_count - 1
                    ) or can_sum_to_target(target, items_count - 1)

            return dp[items_count][target]
            # initialize dp[target][items_count]
            """
          - we can select the current number at nums[item_count-1], or we can simply ignore it:
            - if we select it, the new_target = target - nums[item_count-1]
            - otherwise, we reserve the target.
          - In either ways, dp[target][items_count] = can_sum_to_target(target-nums[item_count-1], items_count-1) 
            or can_sum_to_target(target, items_count-1)
          - return dp[items_count][target]


          base_case: 
          - if target == 0: return True
          - elif items_count is equal to 0: return False
          """

        return can_sum_to_target(target, len(nums)) == 1
