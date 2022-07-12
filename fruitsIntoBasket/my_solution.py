# https://leetcode.com/problems/fruit-into-baskets
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        fruits_count = dict()
        start = 0
        fruits_count[fruits[0]] = fruits_count.get(fruits[0], 0) + 1

        ans = 2
        # We start tracking from the second element
        end = 1

        while end < len(fruits):
            fruits_count[fruits[end]] = fruits_count.get(fruits[end], 0) + 1

            fruit_types = len(fruits_count)
            # We are using start <= end because a subarray with the length of 1 (in case start == end) will always make a valid
            # subarray for fruit_types <= 2
            while start < end and fruit_types > 2:
                fruits_count[fruits[start]] = fruits_count.get(
                    fruits[start], 0) - 1
                if fruits_count[fruits[start]] <= 0:
                    del fruits_count[fruits[start]]
                # if fruit_types exceeds the limit of 2, we must reduce fruits from the start bound until fruit_types == 2 again
                fruit_types = len(fruits_count)
                start += 1
            ans = max(ans, end - start + 1)
            end += 1

        return ans
