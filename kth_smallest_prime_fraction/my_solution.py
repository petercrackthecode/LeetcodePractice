# https://leetcode.com/problems/k-th-smallest-prime-fraction/
import heapq
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fraction_arr = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                fraction = arr[i] / arr[j]
                fraction_arr.append((fraction, arr[i], arr[j]))

        heapq.heapify(fraction_arr)

        (_, numerator, denomerator) = heapq.nsmallest(k, fraction_arr)[k-1]

        return [numerator, denomerator]
