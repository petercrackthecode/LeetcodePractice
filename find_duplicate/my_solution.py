# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        position starting from 1 -> n+1
        use the array nums as pointers, where each element nums[i] will point to the position nums[i] next
        get the last index of nums (len(nums[i]) - 1)
        have two pointers, fast and slow, both initialized to nums[-1]
        fast will move two steps at the time, while slow will move 1 step at a time.
        loop: repeatedly move fast and slow with their respectives steps while fast != slow or fast == nums[-1]

        moving a pointer: if we are at the index i, we'll move to nums[i] - 1 next (because index = position - 1)
        once fast meets slow, we're at the cycle. have a pointer call entry = nums[-1]
        keep moving slow by 1 step and entry by 1 step respectively until nums[slow-1] == nums[entry-1]

        return entry

        transforming a pointer: temp = nums[temp-1]
        """
        fast = slow = nums[-1]
        moved_once = False
        while fast != slow or not moved_once:
            fast = nums[fast-1]
            moved_once = True
            fast = nums[fast-1]
            slow = nums[slow-1]
        entry = nums[-1]
        while slow != entry:
            slow = nums[slow-1]
            entry = nums[entry-1]

        return entry
