# https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        have two pointers fast and slow where slow moves 1 step at a time and fast moves 2 steps at a time. Both fast and slow initialized to the head of the linked list.
        loop while fast and fast.next are both not null:
        - move fast 2 steps.
        - move slow 1 step.
        return slow- it's the middle node of the linked list. 
        """
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
