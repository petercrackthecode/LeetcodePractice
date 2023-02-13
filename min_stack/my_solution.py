# https://leetcode.com/problems/min-stack/
from collections import deque


class MinStack:
    """
    - Use a deque to represent a stack.
    - Every time we push an element into our stack, we gotta find a way to keep track of its for max and min.
    - Maybe we can have a stack called min_so_far which save the current min element in the stack.
    - Because every time we pop an element from our stack, it's just a revert step of the previous push.
    """

    def __init__(self):
        self.min_so_far = deque()
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

        current_min = float('inf')

        if len(self.min_so_far) == 0 or val < self.min_so_far[-1]:
            current_min = val
        else:
            current_min = self.min_so_far[-1]
        self.min_so_far.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_so_far.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_so_far[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
