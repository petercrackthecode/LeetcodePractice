# https://leetcode.com/problems/find-k-closest-elements
from typing import List
import functools


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = 3

        k closest integers to x in the array.

        *** Bruteforce:
        - Sort arr ascendingly based on each element's distance to x (have a helper function called cmp_by_dist_to_x(a:int, b:int) to help us do so): arr.sort(key=functools.cmp_to_key(cmp_by_dist_to_x))
        - return arr[:k]
        """

        def cmp_by_dist_to_x(a: int, b: int) -> int:
            a_dist: int = abs(a - x)
            b_dist: int = abs(b - x)

            return a_dist - b_dist if a_dist != b_dist else a - b

        arr.sort(key=functools.cmp_to_key(cmp_by_dist_to_x))

        return sorted(arr[:k])
