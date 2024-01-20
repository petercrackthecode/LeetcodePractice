# https://leetcode.com/problems/student-attendance-record-i/description/
class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        - have a variable called is_absent_before = False
        - Iterate thru every character in s at position i ([0, len(s) - 1]). For each character ch = s[i]
            - if ch is equal to 'A':
                - if is_absent_before:
                    return False immediately
                - otherwise, is_absent_before = True
            - otherwise, if ch is equal to 'L':
                - if i is smaller than or equal to len(s) - 3:
                    - if s[i+1] and s[i+2] are both equal to 'L':
                        - return False imediately.

            - return True

        0123 | 4
        LLLA
        """
        is_absent_before = False
        for i, ch in enumerate(s):
            if ch == 'A':
                if is_absent_before:
                    return False
                is_absent_before = True
            elif ch == 'L':
                if i <= len(s) - 3 and s[i+1] == s[i+2] == 'L':
                    return False

        return True
