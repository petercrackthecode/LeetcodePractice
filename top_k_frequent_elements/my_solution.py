# https://leetcode.com/problems/top-k-frequent-elements/
from typing import Set, List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        have a dictionary called group_nums_by_freq:
        - key: the frequency: int
        - value: a set of numbers with the same frequencies (key): Set[int]
        have a dictionary called freq_lookup:
        - key: a number: int
        - value: the count of that number in nums

        traverse through every single number in nums to initialize group_nums_by_freq:

        group_nums_by_freq = defaultdict(set)
        freq_lookup = defaultdict(int)
        ans = []

        for num in nums:
            freq = freq_lookup[num]
            if freq > 0 and freq in group_nums_by_freq:
                group_nums_by_freq[freq].discard(num)
            new_freq = freq + 1
            freq_lookup[num] = new_freq
            group_nums_by_freq[new_freq].add(num)

        for (freq, same_freq_nums) in group_nums_by_freq:
            if k <= 0:
                break
            ans += list(same_freq_nums)[0:k] # only take up to k elements top
            k -= len(same_freq_nums)

        return ans
        """
        group_nums_by_freq = defaultdict(set)
        freq_lookup = defaultdict(int)
        ans = []

        for num in nums:
            freq = freq_lookup[num]
            if freq > 0 and freq in group_nums_by_freq:
                group_nums_by_freq[freq].discard(num)
            new_freq = freq + 1
            freq_lookup[num] = new_freq
            group_nums_by_freq[new_freq].add(num)

        keys_in_descending_order = list(reversed(group_nums_by_freq.keys()))

        for freq in keys_in_descending_order:
            same_freq_nums = group_nums_by_freq[freq]
            if k <= 0:
                break
            ans += list(same_freq_nums)[0:k]  # only take up to k elements top
            k -= len(same_freq_nums)

        return ans
