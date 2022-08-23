# https://leetcode.com/problems/backspace-string-compare/
from collections import deque


def apply_character_operation_to_stack(char, stack):
    if char == "#":
        if len(stack) > 0:
            stack.pop()
    else:
        stack.append(char)


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = deque()
        t_stack = deque()

        for char in s:
            apply_character_operation_to_stack(char, s_stack)

        for char in t:
            apply_character_operation_to_stack(char, t_stack)

        operated_s = "".join(char for char in s_stack)
        operated_t = "".join(char for char in t_stack)

        return operated_s == operated_t
