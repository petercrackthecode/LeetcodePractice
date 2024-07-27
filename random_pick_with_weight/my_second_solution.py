# https://leetcode.com/problems/random-pick-with-weight/
from typing import List, Tuple
from random import randint


class Solution:

    def __init__(self, weights: List[int]):
        #                           (start (inclusive), end (non_inclusive))
        self.cumulative_sums: List[Tuple[int, int]] = []
        curr_start: int = 0

        for weight in weights:
            self.cumulative_sums.append((curr_start, curr_start + weight))
            curr_start += weight
        self.random_ceiling_exclusive: int = curr_start

    def pickIndex(self) -> int:
        rand_num: int = randint(0, self.random_ceiling_exclusive - 1)

        def find_num_idx_range(num: int) -> int:
            left, right = 0, len(self.cumulative_sums) - 1

            while left <= right:
                mid: int = left + (right - left) // 2
                if self.cumulative_sums[mid][0] <= num < self.cumulative_sums[mid][1]:
                    return mid
                elif self.cumulative_sums[mid][1] <= num:  # move right
                    left = mid + 1
                else:  # move left
                    right = mid - 1
            return 0

        return find_num_idx_range(rand_num)
