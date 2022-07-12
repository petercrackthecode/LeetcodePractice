# https://leetcode.com/problems/fruit-into-baskets
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        most = 0
        count = 0
        kinds = 0
        basket = set()
        for i in range(len(fruits)):
            if fruits[i] in basket:
                count += 1
            else:
                kinds += 1
                if kinds > 2:
                    kinds = 2
                    basket.clear()
                    j = i - 1
                    consecutive = 1
                    while fruits[j-1] == fruits[j]:
                        j -= 1
                        consecutive += 1
                    basket.add(fruits[j])
                    basket.add(fruits[i])
                    count = consecutive + 1
                else:
                    basket.add(fruits[i])
                    count += 1

            most = max(count, most)

        return most
