from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        have two pointers- fast and slow. the fast pointer move 2 steps at a time, where the slow pointer moves one step at a time.
        initialized both fast and slow to head
        move the fast pointer 2 steps:
        - step 1: if fast reaches the nullptr. return False.
        - step 2: if fast reaches the nullptr. return False. otherwise, if fast equals to slow, return True.
        Move the slow pointer 1 step.
        Repeat the two steps above while fast != slow.
        """
        # edge case: empty node or a single node with no cycle: return False
        if not head or not head.next:
            return False

        fast = head
        slow = head
        while True:
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            if not fast:
                return False
            elif fast == slow:
                return True

            slow = slow.next

        return False
