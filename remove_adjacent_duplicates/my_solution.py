# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
from collections import deque


class Solution:
    def removeDuplicates(self, s: str) -> str:
        char_stack = deque()

        for char in s:

            if len(char_stack) == 0:
                char_stack.append(char)
                continue

            if char == char_stack[-1]:
                char_stack.pop()
            else:
                char_stack.append(char)

        return "".join(char_stack)
