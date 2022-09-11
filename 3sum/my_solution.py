# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        + Save all the numbers into a dictionary where a key is the the number and the respective
        value is a set of indices from the nums list whose nums[index] = number.
        + Have a set called valid_triplets which we'll save the valid 3 sum triplets to.
        + Proceed a double for-loop:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    sum_of_two = nums[i] + nums[j]
                    target = -sum_of_two
                    if target in lookup_indices_by_num:
                        target_indices = lookup_indices_by_num[target]
                        for target_index in target_indices:
                            if target_index != i and target_index != j:
                                valid_triplets.add(sorted([i, j, target_index]))
        + Return list(valid_triplets)
        """
        # key: number
        # value: a set of indices from the nums list whose nums[index] = number
        lookup_indices_by_num = dict()
        for id, num in enumerate(nums):
            if num not in lookup_indices_by_num:
                lookup_indices_by_num[num] = set()
            lookup_indices_by_num[num].add(id)
        valid_triplets = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum_of_two = nums[i] + nums[j]
                target = -sum_of_two
                if target in lookup_indices_by_num:
                    target_indices = lookup_indices_by_num[target]
                    for target_index in target_indices:
                        if target_index != i and target_index != j:
                            sorted_triplet_list = sorted(
                                [nums[i], nums[j], nums[target_index]])
                            valid_triplets.add(
                                (sorted_triplet_list[0], sorted_triplet_list[1], sorted_triplet_list[2]))
        return list(valid_triplets)
