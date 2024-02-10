from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(N) | N = the length of the linked list
# Space: O(N)
class Solution:
    def reverseList(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if head == None or head.next == None:
            return head
        ans = None

        while head != None:
            temp = ans if ans != None else None
            ans = ListNode(head.val, temp)
            head = head.next

        return ans
