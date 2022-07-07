# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
from typing import Optional


class Solution:
    def __init__(self):
        self.reverse_list: Optional[ListNode] = None
        self.temp: Optional[ListNode] = None

    def reverseListRecursively(self, node: Optional[ListNode]) -> None:
        if not node:
            return

        self.reverseListRecursively(node.next)

        if not self.reverse_list:
            self.reverse_list = ListNode(node.val)
            self.temp = self.reverse_list
        else:
            self.temp.next = ListNode(node.val)
            self.temp = self.temp.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.reverseListRecursively(head)
        return self.reverse_list
