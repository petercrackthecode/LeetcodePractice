# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        - sort nums
        - return the elements kth position from the last element: nums[-k]

        Time: O(NlogN)
        Space: O(1)
        '''
        nums.sort()

        return nums[-k]