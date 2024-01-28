# https://leetcode.com/problems/min-stack/
from collections import deque


class MinStack:
    """
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    top                                                                         0
    min:   None -> -2  ->  -2.    ->  -3.            -3              -2         -2            -2
    stack: []  -> [-2] -> [-2, 0] -> [-2, 0, -3] -> [-2, 0, -3] -> [-2, 0] -> [-2, 0] -> [-2, 0]

    => maintain the min_so_far and a min_stack as the stack being pushed and popped. min_stack should have the same size as our main stack (len(self.min_stack) == len(self.stack))
min_so_far:[]. -> [-2] -> [-2,-2] -> [-2,-2,-3]  -> [-2, -2, -3]-> [-2,-2] -> [-2,-2] -> [-2,-2]
    """

    def __init__(self):
        """
        initializes the stack object
        - the last element in self.min_stack (self.min_stack[-1]) is always the smallest element so far in our stack
        """
        self.stack = deque()
        self.min_stack = deque()

    # push the element val onto the stack
    def push(self, val: int) -> None:
        min_so_far = val if len(self.min_stack) == 0 else min(
            self.min_stack[-1], val)
        self.stack.append(val)
        self.min_stack.append(min_so_far)

    # remove the element on top of the stack
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    # get the top element in the stack
    def top(self) -> int:
        return self.stack[-1]

    # get the minimum element in the stack.
    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
