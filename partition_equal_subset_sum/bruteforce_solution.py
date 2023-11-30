# https://leetcode.com/problems/partition-equal-subset-sum/
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        can_partition = False
        """
        have 2 list called first and second. initialized the first list to nums & the second list as an empty list.
        have 2 variables first_sum = sum(nums) and second_sum = 0
        sequentially take an element from the first list at position (0 -> len(first) - 1) and push it to the second list, form a 2 new lists accordingly. Then, update first_sum and second_sum (new_first_sum = first_sum - popped_elem, new_second_sum = second_sum + popped_elem)
        have a helper function called can_partition_helper(first, first_sum, second_sum)
        can_partition_helper's base case:
            when first_sum == second_sum or len(first_sum) == 0:
                if first_sum == second_sum, update can_partition to True

        within canPartition, call can_partition_helper(nums, sum(nums), 0)
        return can_partition
        """
        def can_partition_helper(first: List[int], first_sum: int, second_sum: int) -> None:
            nonlocal can_partition
            if first_sum == second_sum:
                can_partition = True
                return
            elif len(first) == 0:
                return
            # first_sum != second_sum and len(first) > 0
            for i in range(len(first)):
                new_first_sum = first_sum - first[i]
                new_first = first[0:i] + first[i+1:]
                new_second_sum = second_sum + first[i]
                can_partition_helper(new_first, new_first_sum, new_second_sum)

        can_partition_helper(nums, sum(nums), 0)

        return can_partition
