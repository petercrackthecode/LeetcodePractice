# https://leetcode.com/problems/multiply-strings/
from collections import deque


def add_two_num(num1: str, num2: str) -> str:
    # a list of characters, using deque for better prepend
    ans = deque([])
    num1_array = [char for char in num1]
    num2_array = [char for char in num2]
    is_adding_one_to_next_degree = False
    while len(num1_array) > 0 and len(num2_array) > 0:
        curr_sum = int(num1_array.pop(-1)) + int(num2_array.pop(-1)
                                                 ) + (1 if is_adding_one_to_next_degree else 0)
        ans.appendleft(str(curr_sum % 10))
        is_adding_one_to_next_degree = curr_sum >= 10

    while len(num1_array) > 0:
        curr_sum = int(num1_array.pop(-1)) + \
            (1 if is_adding_one_to_next_degree else 0)
        ans.appendleft(str(curr_sum % 10))
        is_adding_one_to_next_degree = curr_sum >= 10

    while len(num2_array) > 0:
        curr_sum = int(num2_array.pop(-1)) + \
            (1 if is_adding_one_to_next_degree else 0)
        ans.appendleft(str(curr_sum % 10))
        is_adding_one_to_next_degree = curr_sum >= 10

    if is_adding_one_to_next_degree:
        ans.appendleft("1")

    return ''.join(ans)


def multiply_a_number_to_a_digit(num: str, digit: str) -> str:
    num_iterator = len(num) - 1
    ans = deque()
    memoized_addition = 0
    while num_iterator >= 0:
        curr_product = int(num[num_iterator]) * int(digit) + memoized_addition
        ans.appendleft(str(curr_product % 10))
        memoized_addition = curr_product // 10

        num_iterator -= 1
    if memoized_addition > 0:
        ans.appendleft(str(memoized_addition))

    return ''.join(ans)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = "0"
        # an array of string numbers that save the result of each multiplication
        multiplied_results = []
        longer_number = num1 if len(num1) >= len(num2) else num2
        shorter_number = num1 if len(num1) < len(num2) else num2
        shorter_number_length = len(shorter_number)

        for degree in range(shorter_number_length):
            curr_result = (multiply_a_number_to_a_digit(
                longer_number, shorter_number[shorter_number_length - 1 - degree])) + ("0" * degree)
            multiplied_results.append(curr_result)

        for result in multiplied_results:
            ans = add_two_num(ans, result)

        # Remove trailing zeroes
        deque_answer = deque(ans)
        while deque_answer[0] == '0' and len(deque_answer) > 1:
            deque_answer.popleft()

        return ''.join(deque_answer)
