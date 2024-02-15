# https://leetcode.com/problems/reverse-linked-list-ii/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_sub_list(start: Optional["ListNode"], end: Optional["ListNode"]) -> None:
    if not start or not end:
        return

    prev, curr, _next = None, start, None
    terminated_node = end.next
    while curr != terminated_node:
        _next = curr.next
        curr.next = prev

        prev = curr
        curr = _next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """
        we have a linked list with n nodes, reverse the sub linked list from the left-th nodes to the right-th nodes (inclusively)
        1 <= left <= right <= n

        - if left == right: no reversal needed => return immediately.

        - have a variable called counter = 1.
        - new_head = None
        - temp = head
        - have a variable called before to save the node at the (left-1)-th position. before = None
        - loop while temp is not null and counter is smaller than left:
            - before = temp
            - temp is equal to temp.next
            - increment counter by 1.
        # counter == left
        - have a helper function call reverse_sub_list(start: Optional["ListNode"], end: Optional["ListNode"]) -> None to reverse a sub linked list.
        - start = temp
        - have a node moved (right-left - 1) next moves from start called end.
        - after = end.next
        - call reverse_sub_list(temp, end)
        # end is now the first node in the sub list
        # start is the last node in the sub list
        - if left == 1 => we have new head: assign new_head = end if new_head is null.
        - before.next = end

        - start.next = after

        - if left == 1: return new_head.
        - Otherwise, return head.


        1 -> 2 -> 3 -> 4 -> 5
        left = 1
        right = 3

        3 -> 2 -> 1 -> 4 -> 5
        """
        if left == right:
            return head
        # left < right
        nodes_count = 1
        new_head = None
        temp = head
        before = None

        while temp and nodes_count < left:
            before = temp
            temp = temp.next
            nodes_count += 1
        # counter == left
        start = temp
        moves = right - left
        end = start
        while moves > 0:
            end = end.next
            moves -= 1

        after = end.next
        reverse_sub_list(start, end)
        # if left == 1 => we have new head: assign new_head = end if new_head is null.
        new_head = end if left == 1 and not new_head else new_head

        if before:
            before.next = end
        start.next = after

        return new_head if left == 1 else head
