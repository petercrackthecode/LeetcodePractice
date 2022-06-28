from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Pos: position of the node where the cycle starts

        Two pointers technique: Have 2 pointers starting at the same position, but one pointer moves twice as fast as the other. Let's call the the pointer that moves twice as fast two_steps, and the pointer that moves at the normal pace (1 step at a time) one_step.
        We know that we have a cycle, two_steps will meet one_step at some point during its traversal. Then, we'll return True. Otherwise, once two_steps reach the end of the linked list without hitting one_step, we'll return False.
        """

        one_step = two_steps = head

        while two_steps and one_step:
            two_steps = two_steps.next
            if two_steps != None and one_step == two_steps:
                # cycle detected!
                return True
            if not two_steps:
                # We've hit the end of the linked list without finding a cycle
                return False

            two_steps = two_steps.next
            if two_steps != None and one_step == two_steps:
                # cycle detected!
                return True
            if not two_steps:
                # We've hit the end of the linked list without finding a cycle
                return False
            one_step = one_step.next

        return False
