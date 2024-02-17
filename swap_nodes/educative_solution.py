# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional["ListNode"], k: int) -> Optional["ListNode"]:
        """
                k = 5
                 1 2 3 4 5 6 7 8 9 10
        in:     [7,9,6,6,7,8,3,0,9,5]
        out:    [7,9,6,6,8,7,3,0,9,5]

                 k = 2
                 h
                    b
                          e
                [1, 2, 3, 4, 5]
                - from the head, get the node k nodes from the beginning

                - start from head, moves k-1 steps:
                    - temp = head
                    - moves = k - 1
                    - while moves is greater than 0 and temp is not null:
                        - temp is equal to temp.next
                        - moves is decremented by 1
                - k_from_start = temp
                - to get the node k nodes from the end, use the two pointer approach:
                    - have a node called before = head.
                    - have a node called after  = head
                    - move after k-1 moves from before.
                    - while after.next is not null, repeat these steps:
                        - before = before.next
                        - after = after.next
                    - before now is the node k nodes from the end of the list.

                - swap the value at k_from_start with the value at before, and vice versa.

                return head.
        """
        temp = head
        nodes_count = 1

        while nodes_count < k and temp:
            temp = temp.next
            nodes_count += 1
        # nodes_count == k
        front = temp
        end = head

        while temp and temp.next:
            temp = temp.next
            end = end.next

        front.val, end.val = end.val, front.val

        return head
