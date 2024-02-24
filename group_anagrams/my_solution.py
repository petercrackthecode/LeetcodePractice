# https://leetcode.com/problems/group-anagrams/
from typing import List, DefaultDict
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        - ans = []
        - have a dictionary called word_groups: key: the sorted version of the words: str, value: the list of all anagrams that form the said word: List[str], to group the anagrams together. word_groups = defaultdict(kust)

        - iterate thru strs: for each string s in strs:
            - sorted_str = sorted(s)
            - add s to word_groups[sorted_str]
        - iterate thru each group in word_groups.values():
            - append group to ans

        - return ans
        Time: O(N)
        Space: O(N)
        """
        ans: List[List[str]] = []
        word_groups: DefaultDict[str, List[str]] = defaultdict(list)

        for s in strs:
            sorted_str: str = "".join(sorted(s))
            word_groups[sorted_str].append(s)

        for group in word_groups.values():
            ans.append(group)

        return ans
