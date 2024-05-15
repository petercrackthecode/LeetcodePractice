# https://leetcode.com/problems/combination-sum/
from typing import List

"""
Constraints:
* 1 <= candidates.length <= 30
* 2 <= candidates[i] <= 40
* All elements of candidates are distinct.
* 1 <= target <= 40
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        - Initialize an array, arr, to store the combinations.
        - For each value i, from 0 to target, iterate over nums and use previous results from arr to calculate
        all combinations that sum up to i.
        - Store all newly calculated combinations at arr[i]
        - Return arr[target], which contains all the combinations that sum up to target.

        candidates = [2,3,6,7], target = 7
        output     = [[2, 2, 3], [7]]

        - sort candidates ascendingly first

        arr = [[],]
        each list at index i in arr represents the combination that sum up to i
        curr_target = 3

        arr[1] = [] # the list of all lists whose sum is 1
        arr[2] = [map(lambda lst: lst + [2], arr[2-2])]
        arr[3] = [map(lambda lst: lst + [2], arr[3-2])] + [map(lambda lst: lst + [3], arr[3-3])]

           *
        [2,3,6,7]

        - sort candidates ascendingly
        - have a list of list called lists_with_sum:List[List[int]] = [[] for _ in range(target)] to save the list of
        - set the lists_with_sum[0] as a list of empty list of int: (lists_with_sum[0] = [[]])- since for the target == 0, we only have an empty combination to return
        list whose sum is equal to a target.
        - loop for curr_target = 2 -> target:
          - loop for candidate in candidates:
            - if curr_target < candidate:
              - break the loop.
            - otherwise (curr_target >= candidate):
              - get the remainder
              - get a new list of new_combis = [sorted(lst + [candidate]) for lst in lists_with_sum[remainder])]
              - loop: for each combination in new_combis:
                - if combination doesn't exist in lists_with_sum[curr_target]: append combination to lists_with_sum[curr_target]

        - return lists_with_sum[target]
        """
        candidates.sort()
        # lists_with_sum[target] represents a list of all the lists of each whose sum is target
        lists_with_sum: List[List[List[int]]] = [[] for _ in range(target + 1)]
        lists_with_sum[0] = [[]]

        for curr_target in range(2, target + 1):
            for candidate in candidates:
                if curr_target < candidate:
                    break
                else:  # curr_target >= candidate => remainder >= 0
                    remainder: int = curr_target - candidate

                    lists_with_remainder_sum: List[List[int]] = lists_with_sum[
                        remainder
                    ]

                    new_combis: List[List[int]] = [
                        sorted(lst + [candidate]) for lst in lists_with_remainder_sum
                    ]
                    for combi in new_combis:
                        if combi not in lists_with_sum[curr_target]:
                            lists_with_sum[curr_target].append(combi)

        return lists_with_sum[target]
