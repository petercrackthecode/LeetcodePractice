# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        - is candidates sorted?
            - no: sort candidates ascendingly

        [2, 3, 6, 7]
        target = 7

        pick forward: pick the numbers at index after the current index i
        [2, 2, 3]
        [3, ] 4

        - have a variable called ans:List[List[int]] = []
        - pick the number at index i: new_target:int = target - candidates[i]
        - see if we can form new_target from any numbers at index i and so on.
        - if new_target >= candidates[i]: repeat the steps above.

        - sort candidates ascendingly
        - have a list of List[int] called ans: ans:List[List[int]] = []
        - have a helper function called combination_sum_helper(start_idx: int, target: int, combi:List[List[int]]) -> None to help us calculate all the combinations & save the combination that makes the target == 0 to ans
        - combination_sum_helper function:
            - if target equals 0, append combi to ans & return.
            - otherwise, loop from index i = start -> len(candidates) - 1:
                - if candidates[i] is greater than target (then candidates[i+1], candidates[i+2], etc. will also be greater than target) => we cannot form a valid combination from the numbers within the range => break the loop.
                - otherwise, add candidates[i] to our existing combination: new_combi:List[List[int]] = combi + [candidates[i]]
                - subtract candidates[i] from target to get a new target: new_target:int = target - candidates[i]
                - call the function combination_sum_helper on the new set of start index, new_target, and new_combi: combination_sum_helper(i, new_target, new_combi) (we reuse i as the start index because we may can still subtract candidates[i] from new_target to form a combination)

        - return ans
        """
        candidates.sort()
        ans: List[List[int]] = []

        def combination_sum_helper(
            start: int, target: int, combi: List[List[int]]
        ) -> None:
            nonlocal ans, candidates

            if target == 0:
                ans.append(combi)
                return

            # target > 0
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                # candidates[i] <= target
                new_target: int = target - candidates[i]
                new_combi: List[List[int]] = combi + [candidates[i]]

                combination_sum_helper(i, new_target, new_combi)

        combination_sum_helper(0, target, [])

        return ans
