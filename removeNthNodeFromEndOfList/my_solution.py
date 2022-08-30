# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        first = second = head
        while n > 0:
            second = second.next
            n -= 1

        while second and second.next:
            first = first.next
            second = second.next
        if second == None:
            # Delete the nth node from the tail- head node
            head = head.next
        else:
            first.next = first.next.next

        return head
