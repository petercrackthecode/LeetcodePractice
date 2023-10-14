# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        """
        Time complexity: O(2^N) where N = len(candidates)
        Space complexity: O(N * K) where K is the maximum depth of the recursive call stack, which
        depends on the number of valid combinations

                      0 1 2 3
        candidates = [2,3,6,7], target = 7

        Brute force: 2 + 2
                           + 2
                           + 3
                     2 + 3
                     2 + 6

                     3 + 3
                     3 + 6
                           + 7
                     ....

                     6 + 6
                     6 + 7

        - have a variable called ans = []
        - have a helper function called form_combination(index: int, comb: List[int], comb_sum: int) -> None that forms numbers combination from the given index.
        - iterate from all positions 0..len(candidates) - 1 to pass them as the start index for form_combination:
            for i in range(len(candidates)):
                comb = [candidates[i]]
                comb_sum = candidates[i]
                form_combination(i, comb, comb_sum)

        - return ans

        form_combination(index: int, comb: List[int], comb_sum: int) -> None:
        - to avoid overlap, we won't go back to pick any number before index (index-1, index-2, etc.)
        - check if comb_sum == target, then we have a valid combination => add comb to ans:
            ans.append(comb)
        - elif comb_sum > target, stop the loop immediately.
        - else: # comb_sum < target
            for j in range(index, len(candidates)):
                new_comb_sum = comb_sum + candidates[j]
                new_comb = list(comb) + [candidates[j]]
                form_combination(j, new_comb, new_comb_sum)
        """
        ans = []

        def form_combination(i: int, comb: List[int], comb_sum: int) -> None:
            if comb_sum == target:
                ans.append(comb)
            elif comb_sum > target:
                return
            else:  # comb_sum < target
                for j in range(i, len(candidates)):
                    new_comb_sum = comb_sum + candidates[j]
                    new_comb = list(comb) + [candidates[j]]
                    form_combination(j, new_comb, new_comb_sum)

        for i in range(len(candidates)):
            comb = [candidates[i]]
            comb_sum = candidates[i]
            form_combination(i, comb, comb_sum)

        return ans
