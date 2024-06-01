# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        The division between 2 integers always rounded toward 0?
        - a/b = x (x is a floating point number):
            - if x >= 0:
                - round down
            - otherwise:
                - round up.

        ["2","1","+","3","*"]

        nums = [9]
        ops  = 

                           *
        ["4","13","5","/","+"]
        nums:List[int] = [6]

                                                              *
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        nums = [22] 

        - whenever we have an operator, we pop 2 most recent numbers from nums and apply the operator to them.
        - when we have the result of the above calculation, we append it back to our nums stack.
        - since our RPN notation is always valid, whenever we face an operator, our nums stack always has at least 2 elements to pop from (no exception handling needed.)

        ** ALGORITHM:
        - have a stack called nums:List[int] to push all the numbers as we traverse thru tokens.
        - loop: for each token in tokens:
            - if token is a number (token not in {"+", "-", "*", "/"}):
                - convert token to an integer: num:int = int(token)
                - append num to nums: nums.append(num)
            - otherwise, token is a operators:
                - pop 2 elements first & second from nums:
                    - second:int = nums.pop()
                    - first:int = nums.pop()
                - if token equals to "*":
                    - result = first * second
                - otherwise, if token equals "+":
                    - result = first + second
                - otherwise, if token equals "-":
                    - result = first - second
                - otherwise, token is division:
                    - result = first / second
                    - if result is greater than or equal to 0: result = math.floor(result)
                    - otherwise, result equals math.ceil(result)
                - append result back to nums
            
            - return nums[-1]

- have a stack called nums:List[int] to push all the numbers as we traverse thru tokens.
- loop: for each token in tokens:
    - if token is a number (token not in {"+", "-", "*", "/"}):
        - convert token to an integer: num:int = int(token)
        - append num to nums: nums.append(num)
    - otherwise, token is a operators:
        - pop 2 elements first & second from nums:
            - second:int = nums.pop()
            - first:int = nums.pop()
        - if token equals to "*":
            - result = first * second
        - otherwise, if token equals "+":
            - result = first + second
        - otherwise, if token equals "-":
            - result = first - second
        - otherwise, token is division:
            - result = first / second
            - if result is greater than or equal to 0: result = math.floor(result)
            - otherwise, result equals math.ceil(result)
        - append result back to nums
    
    - return nums[-1]
        '''
        nums:List[int] = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}: # numbers
                num:int = int(token)
                nums.append(num)
            else: # operators

                second:int = nums.pop()
                first:int = nums.pop()

                if token == '+':
                    result:int = first + second
                elif token == '-':
                    result:int = first - second
                elif token == '*':
                    result:int = first * second
                else: # token is division /
                    raw_res:float = first / second
                    result:int = math.floor(raw_res) if raw_res >= 0 else math.ceil(raw_res)

                nums.append(result)

        return nums[-1]