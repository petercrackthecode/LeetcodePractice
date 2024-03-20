# https://leetcode.com/problems/sliding-window-median/
from typing import List, Dict
from heapq import heappush, heappop


def median_sliding_window(nums: List[int], k: int) -> List[float]:
    # to store the medians
    medians: List[float] = []

    # To keep track of the numbers that need to be removed from the heaps
    outgoing_num: Dict[int, int] = {}

    # Max heap
    small_list: List[int] = []

    # Min heap
    large_list: List[int] = []

    # Initialize the max heap by multiplying each element by -1
    for i in range(0, k):
        heappush(small_list, -nums[i])

    # Transfer the top 50% of the numbers from max heap to min heap
    # while restoring the sign of each number
    for i in range(0, k // 2):
        element = heappop(small_list)
        heappush(large_list, -element)

    # Variable to keep the heaps balanced
    balance: int = 0

    i: int = k

    while True:
        # if the window size is odd
        if k % 2 == 1:
            medians.append(-small_list[0])
        else:
            medians.append((-small_list[0] + float(large_list[0])) / 2)

        # Break the loop if all elements have been processed
        if i >= len(nums):
            break

        # Outgoing number
        out_num: int = nums[i - k]

        # Incoming number
        in_num: int = nums[i]
        i += 1

        # If the outgoing number is from max heap
        if out_num <= -small_list[0]:
            balance -= 1
        else:
            balance += 1

        # Add/Update the outgoing number in the dictionary
        if out_num in outgoing_num:
            outgoing_num[out_num] += 1
        else:
            outgoing_num[out_num] = 1

        # If the incoming number is less than the top of the max heap, add it in that heap
        # Otherwise, add it in the min heap
        if small_list and in_num <= (-small_list[0]):
            balance += 1
            heappush(small_list, -in_num)
        else:
            balance -= 1
            heappush(large_list, in_num)

        # Re-balance the heaps
        if balance < 0:
            heappush(small_list, -large_list[0])
            heappop(large_list)
        elif balance > 0:
            heappush(large_list, -small_list[0])
            heappop(small_list)

        # Since the heaps have been balanced, we reset the balance variable to 0
        # This ensures that the two heaps contain the correct elements for the calculations to be performed on the
        # elements in the next window.
        balance = 0

        # Remove invalid numbers present in the diciionary from top of max heap
        while (-small_list[0]) in outgoing_num and (outgoing_num[-small_list[0]] > 0):
            outgoing_num[-small_list[0]] = outgoing_num[small_list[0] * -1] - 1
            heappop(small_list)

        # Remove invalid numbers present in the hash map from top of min heap
        while large_list and large_list[0] in outgoing_num and (outgoing_num[large_list[0]] > 0):
            outgoing_num[large_list[0]] = outgoing_num[large_list[0]] - 1
            heappop(large_list)

    return medians
