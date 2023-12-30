from collections import deque, defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        if s has fewer than 10 characters, return an empty array
        get all substrings of length 10 of string s, for each string, add it to our dictionary substring_frequency (key: substring: str, value: frequency: int).
        loop thru each items (substr, freq) in substring_frequency.items(): if the freq > 1, add it to our answer list.

        return answer
        """
        if len(s) < 10:
            return []

        answer = []
        substring_frequency = defaultdict(int)
        window = deque([ch for ch in s[:10]])
        substring_frequency[''.join(window)] = 1

        for i in range(10, len(s)):
            window.popleft()
            window.append(s[i])
            substring_frequency[''.join(window)] += 1

        for substr, freq in substring_frequency.items():
            if freq > 1:
                answer.append(substr)

        return answer
