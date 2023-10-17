# https://leetcode.com/problems/shortest-way-to-form-string/description/
class Solution:
    def is_subsequence(self, source: str, target: str) -> bool:
        source_idx = 0
        target_idx = 0

        while source_idx < len(source) and target_idx < len(target):
            if source[source_idx] == target[target_idx]:
                source_idx += 1
                target_idx += 1
            else:
                target_idx += 1

        return source_idx >= len(source)

    def shortestWay(self, source: str, target: str) -> int:
        """
        N = len(source), M = len(target)
        Time: O(N*M)
        Space: O(M)
        """

        ans = len(target)
        source_unique_char = set(source)
        target_char = [ch for ch in target]
        valid_substr = ''

        for idx, ch in enumerate(target_char):
            if ch not in source_unique_char:
                return -1
            valid_substr += ch
            if self.is_subsequence(valid_substr, source):
                if idx != 0:
                    ans -= 1
            else:
                valid_substr = ch

        return ans
