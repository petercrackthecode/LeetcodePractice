# https://leetcode.com/problems/circular-array-loop/
from typing import List


def circular_array_loop(nums: List[int]):
    size = len(nums)
    # Iterate through each index of the array 'nums'.
    for i in range(size):
        # Set slow and fast pointer at current index value
        slow = fast = i

        # Set True in 'forward' if element is positive, set False otherwise.
        forward = nums[i] > 0

        while True:
            # Move slow pointer to one step.
            slow = next_step(slow, nums[slow], size)
            # If cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, forward, slow):
                break

            # Second move of fast pointer.
            fast = next_step(fast, nums[fast], size)
            # if cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, forward, fast):
                break

            # Second move of fast pointer.
            fast = next_step(fast, nums[fast], size)
            # If cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, forward, fast):
                break

            # At any point, if fast and slow pointers meet each other, it indicates that loop has been found
            # return True
            if slow == fast:
                return True
    return False

# a function to calculate the next step


def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result += size
    return result

# A function to detect if a cycle doesn't exist


def is_not_cycle(nums, prev_direction, pointer):
    # Set current direction to True if the current element is positive, set False otherwise.
    curr_direction = nums[pointer] >= 0
    # If current_direction and previous direction is different or moving a pointer takes back to the same
    # value, then the cycle is not possible => we return True, otherwise return False
    if prev_direction != curr_direction or abs(nums[pointer] % len(nums)) == 0:
        return True
    else:
        return False
