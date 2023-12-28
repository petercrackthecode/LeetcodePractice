# https://leetcode.com/problems/reverse-linked-list
from typing import Optional

# Definition for singly-linked list,
class ListNode:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        have three pointers to reverse the list iteratively without extra memory
        edge case: if the list has fewer than or equal to 1 node, return the head itself.
        Otherwise (the list have at least 2 nodes):
            curr = head
            next = head.next
            temp = next.next
            if curr == head:
                curr.next = None
            next.next = curr
            curr = next
            next = temp
        repeat the steps above while next is not null

        return curr
        """
        if not head or not head.next:
            return head
        curr = head
        next = head.next

        while next != None:
            temp = next.next
            if curr == head:
                curr.next = None
            next.next = curr
            curr = next
            next = temp

        return curr
