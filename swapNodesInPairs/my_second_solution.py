from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        """
        head is going to be changed.
        """
        if not head or not head.next:
            return head

        new_head = None
        before = None
        start = head
        end = head.next

        while start and end:
            after = end.next

            end.next = start
            start.next = after

            new_head = end if not new_head else new_head

            if before:
                before.next = end
            before = start

            start = after
            end = None if not start else start.next

        return new_head
