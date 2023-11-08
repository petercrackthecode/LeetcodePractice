# https://leetcode.com/problems/next-greater-element-i/
from collections import deque
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        - Utilize monotonic stack for this problem

        in nums2, for each element, find the next greater element on the right side of that element, then save the result to a dictionary: next_greater:
        - key: element: int
        - value: the number that is greater than element and on the right side of element in nums2

        monotonic stack: numbers pushed in the stack are strictly decreasing: [4, 2, 1] 3
        iterate from right to left of nums2. For each ele, push it to our mono_stack:
        - if ele > mono_stack.top(): keep popping until len(mono_stack) == 0 or ele < mono_stack.top(). Then, next_greater[elem] = mono_stack.top()
        - if len(mono_stack) == 0 (there is no number greater than elem in the stack), next_greater[elem] = -1

        Iterate through nums1: for each elem, look up in next_greater, then push the result to ans.
        """
        ans = []

        mono_stack = deque()
        next_greater = dict()

        for num in reversed(nums2):
            while len(mono_stack) > 0 and mono_stack[-1] < num:
                mono_stack.pop()
            if len(mono_stack) == 0:
                next_greater[num] = -1
            else:
                next_greater[num] = mono_stack[-1]
            mono_stack.append(num)

        for num in nums1:
            next_gr = next_greater[num]
            ans.append(next_gr)

        return ans
