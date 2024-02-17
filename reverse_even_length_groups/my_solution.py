from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_sub_list(start: Optional["ListNode"], end: Optional["ListNode"]) -> None:
    if not start or not end:
        return

    after_end = end.next
    prev, curr, _next = None, start, None

    while curr and curr != after_end:
        _next = curr.next
        curr.next = prev

        prev = curr
        curr = _next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        in:     [5,2,6,3,9,1,7,3,8,4]
        out:    [5,6,2,3,9,1,4,8,3,7]

        have a helper function to reverse the sub linked list in place: reverse_sub_list(start: Optional["ListNode"], end: Optional["ListNode"])
        after reversing the sub-linked list, we gotta update the nodes before and after the sub-linked list as well.
        edge case: the length of the last group may be smaller than or equal to 1 + the length of the second to last group => we gotta keep track of the actual number of moves that we have.
        """
        expected_moves = 1
        temp = head
        before = None
        # after = temp.next

        while temp:
            actual_moves = 1
            start = temp
            while actual_moves < expected_moves and temp.next:
                temp = temp.next
                actual_moves += 1
            end = temp
            after = temp.next
            # edge cases: the length of the last group may be smaller than or equal to 1 + the length of the second to last group
            nodes_count = (
                actual_moves if actual_moves < expected_moves else expected_moves
            )
            # even number of nodes => reverse the list
            if nodes_count % 2 == 0:
                reverse_sub_list(start, end)
                # end is now the start of the sublist, and start is now the end of the sublist.
                if before:
                    before.next = end
                start.next = after
                before = start
            else:
                before = end
            temp = after
            expected_moves += 1

        return head
