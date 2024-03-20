# https://leetcode.com/problems/sliding-window-median/
from heapq import heappush, heappop
from typing import List, Set, Dict, Tuple


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        maintain two heaps:
        - small_nums is a max heap representing the first half of the sorted list.
        - large_nums is a min heap representing the second half of the sorted list.

        we should keep track of the actual number of elements within small_nums and large_nums since we do save outside of the window elements to these two lists, which skew up the actual size (tldr: we cannot use the len() function, but actual variables)

        the small_nums's actual size should always be equal or greater by 1 compared to the large_nums's actual size
        we should save elements as tuples of (num, index) into the heap since we wanna keep track of the outside of the window nodes later.
        """
        # max heap => remember to negate the numbers
        small_nums: List[int] = []
        small_nums_size: int = 0

        # min heap
        large_nums: List[int] = []
        large_nums_size: int = 0

        deleted_nums: Set[Tuple[int, int]] = set()

        ans: List[float] = []
        is_odd: bool = k % 2 == 1

        should_print: bool = True

        def get_median() -> float:
            nonlocal is_odd, small_nums, large_nums, small_nums_size, large_nums_size
            if is_odd:
                return -small_nums[0][0] if small_nums_size > large_nums_size else large_nums[0][0]

            return (-small_nums[0][0] + large_nums[0][0]) / 2

        for i in range(k):
            heappush(small_nums, (-nums[i], i))
            small_nums_size += 1

        for _ in range(k // 2):
            popped = heappop(small_nums)
            val, index = -popped[0], popped[1]
            small_nums_size -= 1
            heappush(large_nums, (val, index))
            large_nums_size += 1

        should_print and print(f"nums = {nums}\n")
        ans.append(get_median())

        for i in range(k, len(nums)):
            should_print and print(f"index = {i}")
            deleted_index = i - k
            deleted_nums.add((nums[deleted_index], deleted_index))

            if len(small_nums) > 0 and nums[i] <= -small_nums[0][0]:
                heappush(small_nums, (-nums[i], i))
                small_nums_size += 1
            else:
                heappush(large_nums, (nums[i], i))
                large_nums_size += 1

            should_print and print(f"deleted_nums = {deleted_nums}")
            should_print and print(f"small_nums_size = {small_nums_size}")
            should_print and print(f"small_nums = {small_nums}")
            should_print and print(f"large_nums_size = {large_nums_size}")
            should_print and print(f"large_nums = {large_nums}")

            while small_nums_size - large_nums_size > 1 or (
                len(small_nums) > 0 and (-small_nums[0][0], small_nums[0][1]) in deleted_nums
            ):
                popped = heappop(small_nums)
                popped = (-popped[0], popped[1])
                small_nums_size -= 1
                if popped in deleted_nums:
                    continue

                heappush(large_nums, popped)
                large_nums_size += 1

            while large_nums_size - small_nums_size > 1 or (
                len(large_nums) > 0 and large_nums[0] in deleted_nums
            ):
                popped = heappop(large_nums)
                large_nums_size -= 1
                if popped in deleted_nums:
                    continue
                heappush(small_nums, (-popped[0], popped[1]))
                small_nums_size += 1

            should_print and print(f"\nsmall_nums_size = {small_nums_size}")
            should_print and print(f"small_nums = {small_nums}")
            should_print and print(f"large_nums_size = {large_nums_size}")
            should_print and print(f"large_nums = {large_nums}\n")

            ans.append(get_median())

        return ans
