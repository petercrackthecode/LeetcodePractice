# https://leetcode.com/problems/min-stack/
class MainStack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


class MinStack:
    # Initializing min and main stack
    def __init__(self):
        self.min_stack = MainStack()
        self.main_stack = MainStack()

    # Pop() removes and returns value from min_stack
    def pop(self):
        self.min_stack.pop()
        # Returns the popped value from main_stack
        return self.main_stack.pop()

    # Pushes values into min_stack
    def push(self, value):
        self.main_stack.push(value)

        # If the min_stack is empty, or the value being pushed is less than
        # the minimum (top) value of min_stack
        if self.min_stack.is_empty() or value < self.min_stack.top():
            # Push this new value to the min_stack
            self.min_stack.push(value)
        else:
            # Keep the minimum value at the top of min_stack
            self.min_stack.push(self.min_stack.top())

    # Returns minimum value from min_stack in O(1) Time
    def min_number(self):
        if self.min_stack.is_empty():
            return None
        else:
            return self.min_stack.top()
