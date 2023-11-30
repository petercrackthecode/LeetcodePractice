# https://leetcode.com/problems/word-pattern/
from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        var: dict = {}
        sl: List[str] = s.split()
        pl: int = len(pattern)
        if pl == len(sl) and len(set(list(pattern))) == len(set(sl)):
            for p in range(pl):
                if pattern[p] not in var.keys():
                    var[pattern[p]] = sl[p]
                else:
                    if var[pattern[p]] != sl[p]:
                        return False
            return True
