from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = deque()
        openBracketsMatcher = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            # Check if the character is an openning bracket
            if char in "{[(":
                openBrackets.append(char)
            else:
                if openBrackets and openBracketsMatcher[openBrackets.pop()] == char:
                    continue
                return False

        # There must be no open brackets left unclosed for our string to be valid.
        return len(openBrackets) == 0
