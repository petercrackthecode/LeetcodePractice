# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        temp = ans

        p1 = list1
        p2 = list2

        def add_node(val: int) -> None:
            nonlocal ans, temp
            if ans == None:
                ans = ListNode(val)
                temp = ans
            else:
                temp.next = ListNode(val)
                temp = temp.next

        while p1 != None and p2 != None:
            if p1.val < p2.val:
                add_node(p1.val)
                p1 = p1.next
            else:
                add_node(p2.val)
                p2 = p2.next

        if p1:
            if ans == None:
                ans = p1
            else:
                temp.next = p1
        else:  # p2 != None
            if ans == None:
                ans = p2
            else:
                temp.next = p2

        return ans
