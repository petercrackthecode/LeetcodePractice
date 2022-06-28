from typing import Optional

# Definition for singly-linked list
# class ListNode:
#   def __init__(self, x):
#     self.val = x
#     self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while fast:
            if fast == slow:
                return True
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next

        return False
