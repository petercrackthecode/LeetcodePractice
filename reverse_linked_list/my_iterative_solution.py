from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        """
        - edge case: if the number of nodes in the linked list is <= 1 (not head or not head.next), return head (we don't need to reverse anything)
        # the number of nodes in the linked list >= 2
        - have three nodes: prev, current, and _next. prev = None, current = head, _next = head.next
        - loop these steps:
            - current.next = prev
            - if _next is None => there no more nodes to reverse: break the loop.
            - otherwise, reassign the nodes to their upcoming positions:
                prev = current
                current = _next
                _next = _next.next

            return current as the new head
        # Iterative approach
        # Time: O(N) | N is the number of nodes in the list
        # Space: O(1)
        """
        if not head or not head.next:
            return head
        prev, current, _next = None, head, head.next

        while True:
            current.next = prev
            if not _next:
                break
            prev, current, _next = current, _next, _next.next

        return current
