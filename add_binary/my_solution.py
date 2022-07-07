# https://leetcode.com/problems/add-binary
class Solution:
    def __init__(self):
        self.is_adding_one_to_the_left = False

    def addBinaryDigit(self, a_digit: str, b_digit: str) -> str:
        ans = '0'

        if a_digit == '1' and b_digit == '1':
            ans = '0' if not self.is_adding_one_to_the_left else '1'
            self.is_adding_one_to_the_left = True
        elif (a_digit == '1' and b_digit == '0') or (a_digit == '0' and b_digit == '1'):
            ans = '0' if self.is_adding_one_to_the_left else '1'
            self.is_adding_one_to_the_left = False if (
                not self.is_adding_one_to_the_left) else True
        elif a_digit == '0' and b_digit == '0':
            ans = '0' if not self.is_adding_one_to_the_left else '1'
            self.is_adding_one_to_the_left = False

        return ans

    def addBinary(self, a: str, b: str) -> str:
        # balance two strings' lengths for easier calculation
        while len(a) < len(b):
            a = "0" + a
        while len(b) < len(a):
            b = "0" + b

        ans = ""

        for i in reversed(range(len(a))):
            ans = self.addBinaryDigit(a[i], b[i]) + ans

        # The remaining one must be addressed if self.is_adding_one_to_the_left == True
        ans = '1' + ans if self.is_adding_one_to_the_left else ans

        return ans
