# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Have a dictionary to check the frequencies of elements appear in the array.
        1. Iterate through the nums list & save the frequencies of each element in to the dictionary's value.
        The dictionary will work on this logic:
        - key: the element.
        - value: the number of times that element appears in the array.
        2. Iterate through the dictionary, and return the key where the value >= n/2
        """
        ele_frequenies = dict()
        for num in nums:
            ele_frequenies[num] = ele_frequenies.get(num, 0) + 1

        for ele, freq in ele_frequencies.items():
            if freq >= len(nums) / 2:
                return ele

        return 1
