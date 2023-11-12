# https://leetcode.com/problems/remove-invalid-parentheses/description/
from collections import deque
from typing import List, Set


def are_valid_parentheses(s: str) -> bool:
    open_brackets_count = 0

    for ch in s:
        if ch == '(':
            open_brackets_count += 1
        elif ch == ')':
            if open_brackets_count == 0:
                return False
            else:
                open_brackets_count -= 1

    return open_brackets_count == 0


def cut_brackets(s: str, num_of_brackets_to_delete: int, start_from: int, deleted_indices: Set[int], valid_brackets: Set[str]) -> None:
    if num_of_brackets_to_delete == 0:
        new_s = ''.join([ch for i, ch in enumerate(s)
                        if i not in deleted_indices])
        if are_valid_parentheses(new_s):
            valid_brackets.add(new_s)

        return

    new_num_of_brackets_to_delete = num_of_brackets_to_delete - 1

    for i in range(start_from, len(s)):
        if s[i] != '(' and s[i] != ')':
            continue

        new_deleted_indices = deleted_indices.union({i})
        new_start = i + 1
        cut_brackets(s, new_num_of_brackets_to_delete, new_start,
                     new_deleted_indices, valid_brackets)


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
             0123456
        s = "()())()"

        ans = ["(())()", "()()()"]

        - find the brackets that makes the string invalid => if we remove them, we have a valid case. Say that the number of said brackets is M
        - recursively delete M brackets at any given position in the string s, and see if the remained string is valid (have a function called is_valid to do so).

        M = 1
             01234567
        s = "(a)())()"
        ans = ["(a())()", "(a)()()"]

        s = "()())()("
        num_of_brackets_to_delete

        have a stack to save the opening brackets: open_brackets
        every time we find a closing bracket:
        - if len(open_brackets) == 0:
            increment the num_of_brackets_to_delete by 1
        - else: pop a bracket from open_brackets.
        Run the procedure above from the beginning till the end of the string.

        After the loop above, add len(open_brackets) to num_of_brackets_to_delete

        Recursively, remove a character from an index (until num_of_brackets_to_delete is 0). For every remained string, check if that string is a valid group of parentheses (call is_valid), and if so, add it to ans.
        - To avoid duplication, inially, ans should be a set.
        - Return list(ans)
        """
        open_brackets_count = 0
        num_of_brackets_to_delete = 0

        for ch in s:
            if ch == '(':
                open_brackets_count += 1
            elif ch == ')':
                if open_brackets_count == 0:
                    num_of_brackets_to_delete += 1
                else:
                    open_brackets_count -= 1

        num_of_brackets_to_delete += open_brackets_count
        if num_of_brackets_to_delete == 0:
            return [s]

        ans = set()
        cut_brackets(s, num_of_brackets_to_delete, 0, set(), ans)

        return list(ans)
