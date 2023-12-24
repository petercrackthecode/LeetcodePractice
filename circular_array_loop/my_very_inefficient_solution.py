# https://leetcode.com/problems/circular-array-loop/
from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """
        return True if there exists a cycle of size k where k > 1

        use the fast and slow pointer approach:
        - we must track all indices within nums
        - we must keep track of the size of our cycle k.
        - since we have a circular array, we must handle the moving forward on the last element & moving backward from the first element cases. Have a helper function called get_next_index(index: int) -> int for that.

        - has_cycle = False (the value we will return in the end)
        - have a set called visited_indices = set()
        - loop thru index 0..len(nums)-1 in nums:
            if index already exists in visited_indices, skip to the next iteration
            otherwise: call the helper function traverse(index) to traverse thru the index until we have found a cycle with the length > 1, or we have hit an index that points to itself.

        traverse(index: int) -> None function:
        - have two pointer fast and slow, both initialized to index.
        - repeat these steps while fast.next is different from fast:
            fast = fast.next
            add fast to visited_indices
            if fast is equal to slow and fast.next is different from fast: we have a cycle: has_cycle = True
            fast = fast.next
            add fast to visited_indices
            if fast is equal to slow and fast.next is different from fast: we have a cycle: has_cycle = True
            slow = slow.next

        - We gotta address the case: every nums[seq[j]] is either positive or negative.
        """
        has_cycle = False
        visited_indices = set()

        def get_next_index(i: int) -> int:
            nonlocal nums
            n = len(nums)
            move = nums[i]
            return (i + move) % n

        def traverse(i: int) -> None:
            nonlocal visited_indices, nums
            fast = slow = i
            visited_indices.add(i)
            # 1 mean positive, -1 mean negative, 0 means a mixed of both negatives and positives (failed condition 2- nums[seq[j]] is either all positive or all negative)
            status = 1 if nums[i] > 0 else -1

            def has_cycle_after_move_fast() -> bool:
                nonlocal fast, slow, visited_indices, has_cycle, status, nums
                fast = get_next_index(fast)
                status = 0 if nums[fast] * status <= 0 else status
                visited_indices.add(i)
                if fast == slow and get_next_index(fast) != fast:
                    # detect a cycle with length > 1
                    if status != 0:
                        has_cycle = True
                    return True
                return False

            while fast != get_next_index(fast):
                if has_cycle_after_move_fast() or status == 0:
                    break
                if has_cycle_after_move_fast() or status == 0:
                    break
                slow = get_next_index(slow)

        for i in range(len(nums)):
            if has_cycle:
                break
            if i in visited_indices:
                continue
            traverse(i)

        return has_cycle
