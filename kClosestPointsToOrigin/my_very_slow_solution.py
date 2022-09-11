# https://leetcode.com/problems/k-closest-points-to-origin/
import functools
import math
from typing import List


def comparator(a: List[int], b: List[int]) -> bool:
    a_distance = math.sqrt(a[0]**2 + a[1]**2)
    b_distance = math.sqrt(b[0]**2 + b[1]**2)

    # if a_distance > b_distance:
    #     return 1
    # elif a_distance < b_distance:
    #     return -1
    # else:
    #     return 1
    return a_distance - b_distance


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=functools.cmp_to_key(comparator))

        return points[:k]
