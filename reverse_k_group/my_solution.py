# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_sub_list(start: Optional["ListNode"], end: Optional["ListNode"]) -> None:
    if not start or not end:
        return

    next_start = end.next

    prev, curr, _next = None, start, None
    # TO DO: reverse the sub linked list
    while curr != next_start and curr:
        _next = curr.next
        curr.next = prev
        prev, curr = curr, _next

    start.next = next_start


"""
- Use a pointer to try to traverse k nodes in the linked list
- If the pointer successfully traverses a group of k nodes, reverse this group.
- Reconnect the reversed group of k nodes with the rest of the linked list.
- Repeat this process until less than k or no nodes are left in the linked list.
"""


class Solution:

    def reverseKGroup(self, head: Optional["ListNode"], k: int) -> Optional["ListNode"]:
        """
        - we should have a helper function called reverse_sub_list(start: Optional[ListNode], end: Optional[ListNode]) that reverse in-place a sub list from start to end.
        - we should know the number of nodes in the list called nodes_count, so each time we iteratively reverse k nodes from the range (start, end), we subtract k from nodes_count.
        - after the first time we reverse a sub linked list, the head end node that we passed into the reverse_sub_list function will be the new head of the entire reverseKGroup linked list.
        =======================================================
        - ans = None
        - nodes_count = 0
        - loop thru the entire linked list from head:
            - temp = head
            - while temp is not null:
                - assign temp.next to temp
                - increment nodes_count by 1
        - start is assigned to head.
        - have a variable called last_tail to save the tail node of the sub range we most recently reversed. last_tail = None
        - loop while nodes_count is greater than or equal to k:
            - end = start
            - moves = k - 1
            - while moves is greater than 0, loop:
                - end = start.next
                - moves is decremented by 1.
            - reverse_sub_list(start, end)
            # start is now tail, and end is now head of the sub linked list.
            - ans = ans if ans != None else end
            - if last_tail is not None, assign last_tail.next = end
            - last_tail is assigned to end
            - decrement nodes_count by k


        - return ans
        """
        ans = None
        nodes_count = 0
        temp = head
        while temp:
            nodes_count += 1
            temp = temp.next

        start = head
        last_tail = None

        while nodes_count >= k:
            end = start
            moves = k - 1
            while moves > 0:
                if end:
                    end = end.next
                moves -= 1

            next_start = end.next if end else None

            reverse_sub_list(start, end)
            ans = ans if ans != None else end
            if last_tail:
                last_tail.next = end
            last_tail = start
            start = next_start

            nodes_count -= k

        return ans
