# https://leetcode.com/problems/odd-even-linked-list/
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # must have at least 2 nodes to perform the group, otherwise return the same list
        if not head or not head.next or not head.next.next:
            return head
        first = head
        second = head.next
        first_temp = first
        second_temp = second
        while first_temp.next and second_temp.next:
            first_temp.next = second_temp.next
            first_temp = first_temp.next
            second_temp.next = first_temp.next
            second_temp = second_temp.next

        first_temp.next = second

        return head
