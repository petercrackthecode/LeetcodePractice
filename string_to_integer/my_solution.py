# https://leetcode.com/problems/string-to-integer-atoi/description/


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) <= 0:
            return 0
        """
        "word is -20"
        - read in the next characters until the next until the next non-digit or the end of the input is reached. The rest of the string is ignored.



        - integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1
        """
        ans = 0
        is_negative: bool = s[0] == "-"

        i: int = 1 if s[0] in {"-", "+"} else 0

        while i < len(s) and s[i].isdigit():
            ans = (ans * 10) + int(s[i])
            i += 1

        ans = -ans if is_negative else ans

        if ans > 2**31 - 1:
            ans = 2**31 - 1
        elif ans < -(2**31):
            ans = -(2**31)

        return ans
