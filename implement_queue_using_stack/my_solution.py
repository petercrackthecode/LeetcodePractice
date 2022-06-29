# https://leetcode.com/problems/implement-queue-using-stacks/
from collections import deque


class MyQueue:

    def __init__(self):
        self.push_stack = deque()
        self.pop_stack = deque()

    def transfer_nodes_from_push_to_pop(self) -> None:
        while len(self.push_stack) > 0:
            node = self.push_stack.pop()
            self.pop_stack.append(node)

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if len(self.pop_stack) == 0:
            self.transfer_nodes_from_push_to_pop()
        return self.pop_stack.pop()

    def peek(self) -> int:
        if len(self.pop_stack) == 0:
            self.transfer_nodes_from_push_to_pop()
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return len(self.push_stack) == 0 and len(self.pop_stack) == 0
