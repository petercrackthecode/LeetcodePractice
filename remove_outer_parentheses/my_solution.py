# https://leetcode.com/problems/remove-outermost-parentheses
from collections import deque


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        - returns parentheses with no-inner parentheses

        s = "( ()() ) (()) (()(()))"
        output = "()()()() (())"

        A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

        - have a stack called brackets = deque() to save the parentheses.
        - have a list of characters called string_so_far = [] to save the valid primitive parenthesis so far.
        - if we face an open parenthesis:
            - if brackets is not empty, append the open parenthesis to string_so_far.
            - add the open parenthesis to brackets.
        - if we face a close parenthesis & the length of brackets is greater than 0:
            - pop an element from brackets
            - after the pop, if the lengh of brackets is 0:
                - concat string_so_far to ans: ans += string_so_far
                - reset string_so_far to an empty array.

        - return ans
        """
        brackets = deque()
        string_so_far = []
        ans = []

        for i, ch in enumerate(s):
            if ch == '(':
                if len(brackets) > 0:
                    string_so_far.append('(')
                brackets.append('(')
            else:  # ch == ')'
                if len(brackets) > 0:
                    brackets.pop()
                    if len(brackets) == 0:
                        ans += string_so_far
                        string_so_far = []
                    else:
                        string_so_far.append(')')
        return ''.join(ans)
