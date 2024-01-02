# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque
from typing import List


class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        mono_queue = deque()
        ans = []

        for i, num in enumerate(nums[:k]):
            while len(mono_queue) > 0 and nums[mono_queue[-1]] < num:
                mono_queue.pop()
            mono_queue.append(i)
        ans.append(nums[mono_queue[0]])

        j = 0

        for i in range(k, len(nums)):
            # cleaning up
            if mono_queue[0] == j:
                mono_queue.popleft()
            j += 1
            while len(mono_queue) > 0 and nums[mono_queue[-1]] < nums[i]:
                mono_queue.pop()
            mono_queue.append(i)
            ans.append(nums[mono_queue[0]])

        return ans
