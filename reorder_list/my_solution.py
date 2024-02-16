# https://leetcode.com/problems/reorder-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional["ListNode"]) -> Optional["ListNode"]:
    prev, curr, _next = None, head, None

    while curr:
        _next = curr.next
        curr.next = prev

        prev = curr
        curr = _next

    return prev


def merge_two_lists(l1: Optional["ListNode"], l2: Optional["ListNode"]) -> None:
    if not l1:
        l1 = l2
    elif not l2:
        return
    else:
        p1 = l1
        p2 = l2
        while p2 and p1:
            """
                     n1
                p1
            l1:  1 -> 2
                     n2
                p2
            l2:  4 -> 3

            """
            next_p1 = p1.next
            next_p2 = p2.next

            p1.next = p2
            p2.next = next_p1

            p1 = next_p1
            p2 = next_p2


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
                0.   1    2  | n = 2 | m = 3
        before: 1 -> 2 -> 3
        after : 1 -> 3 -> 2

                0    1    2    3 | n = 3 | m = 4
                1 -> 2 -> 3 -> 4
                - Count the number of nodes in the list. call it m (m = n + 1)
                - If m is an odd number, from head, we have to move (m//2 + 1) steps to get to the second half of the list.
                - Otherwise (m is an even number), from head, we have to move m//2 steps to get to the second half of the list.
                - have a linked list called second_half to save all the nodes that is going to be at the odd indices in the new linked list.
                - Once we at the second half of the list, reverse that second half list, and make it a separate list.

                - merge the first half of the linked list and second_half together. have a helper function call merge_two_lists(l1: Optional["ListNode"], l2: Optional["ListNode"]) -> None to handle this merge task.
                - return head.
        """
        nodes_count = 0
        temp = head

        while temp:
            nodes_count += 1
            temp = temp.next

        moves: int = (
            (nodes_count // 2 + 1) if nodes_count % 2 == 1 else nodes_count // 2
        )
        second_half: Optional["ListNode"] = head
        before_second_half: Optional["ListNode"] = None
        for _ in range(moves):
            before_second_half = second_half
            if not second_half:
                break
            second_half = second_half.next
        # TO DO: implement reverse_list
        second_half = reverse_list(second_half)
        """
        1 -> 2 -> 3 -> 4
first:  1 -> 2 -> None
sec  :  4 -> 3 -> None
        """
        # make the first half of the original linked list a separate list
        if before_second_half:
            before_second_half.next = None

        merge_two_lists(head, second_half)
