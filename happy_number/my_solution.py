# https://leetcode.com/problems/happy-number/
from collections import deque
from typing import List


class Solution:
    def number_to_digits_list(self, number: int) -> List[int]:
        # constraint: number >= 0
        if number == 0:
            return [0]

        ans = deque()

        while number != 0:
            digit = number % 10
            ans.appendleft(digit)
            number = number // 10

        return list(ans)

    def calculate_sum_of_digit_squares(self, num: int) -> int:
        digits_list = self.number_to_digits_list(num)
        ans = 0
        for digit in digits_list:
            ans += digit**2
        return ans

    def isHappy(self, n: int) -> bool:
        """
        Our naive algorithm can be:
        * Have a function to calculate the sum of the squares of a number's digits:
            - calculate_sum_of_digit_squares(num: int) -> int
        * Have another helper function to translate a number to a list of digits (int) to support the calculate_sum_of_digit_squares function:
            - number_to_digits_list(number: int) -> List[int]:
        * Continuously run the function calculate_sum_of_digit_squares with the number as the input (we save the return of the function to number) until number == 1. We return True then.

        One drawback of the algorithm above is it doesn't detect endless loops wheare the output never reaches 1.
        How do we detect that case?
        A loop never reaches the result of 1 if we have a cycle within that loop: a number after the calculate_sum_of_digit_squares operations reach itself again. How do we detect that?
        Maybe we can save the return of the calculate_sum_of_digit_squares() function to a set. If a return result ever existed in a set, stop a loop and return False immediately.
        """
        sum_of_digit_squares_set = set()

        while n != 1:
            n = self.calculate_sum_of_digit_squares(n)
            if n in sum_of_digit_squares_set:
                return False
            sum_of_digit_squares_set.add(n)

        return True
