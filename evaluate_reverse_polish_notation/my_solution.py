from collections import deque
from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = deque()
        for token in tokens:
            try:
                num = int(token)
                operands.append(num)
            except:
                operator = token
                if len(operands) < 2:
                    raise Exception("Error: invalid RPN chain")
                second_num = operands.pop()
                first_num = operands.pop()
                result = 0

                if operator == '+':
                    result = first_num + second_num
                elif operator == '-':
                    result = first_num - second_num
                elif operator == '*':
                    result = first_num * second_num
                elif operator == '/':
                    division_result = first_num / second_num
                    result = math.floor(
                        division_result) if division_result >= 0 else math.ceil(division_result)

                operands.append(result)

        if len(operands) < 1:
            raise Exception("Error: invalid RPN chain")

        return operands[-1]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
ans = Solution().evalRPN(tokens)
print('ans = ', ans)
