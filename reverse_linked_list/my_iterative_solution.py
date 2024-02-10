from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    class Solution:
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            """
            - Initialize the `prev` and `next` pointers to NULL and set the current pointer to the head node.
            - Traverse the linked list until the current pointer reaches the end of the list.
            - Within the loop, set the `next` pointer to the next node in the list and reverse the current node’s pointer to point to the previous node.
            - Update the `prev` and `curr` pointers.
            - After the loop, the `prev` pointer will point to the last node of the original linked list, so set the head pointer to the `prev` pointer.
            """
            prev, curr, next = None, head, None

            while curr:  # curr != None
                next = curr.next
                curr.next = prev
                prev, curr = curr, next

            return prev
