from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if head == None or head.next == None:
            return head

        dummy = None
        prev = head
        curr = head.next

        head = head.next

        while True:
            prev.next = curr.next
            curr.next = prev
            if dummy != None:
                dummy.next = curr

            dummy = prev

            if prev.next != None:
                prev = prev.next
            else:
                break

            if prev.next != None:
                curr = prev.next
            else:
                break

        return head
