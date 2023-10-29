# https://leetcode.com/problems/rotated-digits/description/
from collections import deque
from typing import List


class Solution:
    def get_digits(self, num: int) -> List[int]:
        output = deque()

        while num > 0:
            digit = num % 10
            num //= 10
            output.appendleft(digit)

        return list(output)

    def is_good_number(self, num: int) -> bool:
        num_digits = self.get_digits(num)

        rotatable_digits = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}

        converted_num_digits = []

        for digit in num_digits:
            if digit not in rotatable_digits:
                return False

            rotated_digit = rotatable_digits[digit]
            converted_num_digits.append(rotated_digit)

        return converted_num_digits != num_digits

    def rotatedDigits(self, n: int) -> int:
        output = 0

        for i in range(1, n+1):
            if self.is_good_number(i):
                output += 1

        return output
