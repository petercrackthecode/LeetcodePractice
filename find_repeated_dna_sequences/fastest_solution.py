# https://leetcode.com/problems/repeated-dna-sequences/
from typing import List
from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        a = [s[i:i+10] for i in range(len(s) - 10 + 1)]

        a = Counter(a)
        a = [freq for substr, freq in a.items() if freq > 1]

        return a
