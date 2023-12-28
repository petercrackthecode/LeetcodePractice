from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reversed_linked_list(start: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode]:
    # edge case: the sub-linked list is empty or has only 1 node -> return the start node itself
    if start == end or not start:
        return start
    curr = start
    curr_next = start.next

    while curr != end:
        temp = curr_next.next
        if curr == start:
            curr.next = None
        curr_next.next = curr
        curr = curr_next
        curr_next = temp

    return curr    


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        edge case: if the list has fewer than 2 nodes (not head or not head.next), return True.
        have a node called before_slow which will always be node before slow. before_slow = ListNode(-1, head)
        have two pointers fast and slow initialized to head.
        use the fast and slow pointer approach to move the slow pointer to the middle (if the list has an odd number of nodes) or the second middle (if the list has an even number of nodes) of the list while fast and fast.next. Move fast 2 steps at a time, and move slow and before_slow 1 step at a time.
        reverse all the nodes from head to before_slow. Have a helper function called reversed_linked_list(head, tail) to reverse the linked list from head to before_slow.
        reversed_head = reversed_linked_list(head, before_slow)
        if fast is not null (we have an odd number of nodes in the list), move slow by 1 step.
        loop while slow is not null and reversed_head is not null:
                if slow.val != reversed_head.val:
                    return False 
                reversed_head = reversed_head.next
                slow = slow.next   
        return True
        """
        if not head.next:
            return True
        [fast, slow] = [head, head]
        before_slow = ListNode(-1, head)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            before_slow = before_slow.next
        
        reversed_head = reversed_linked_list(head, before_slow)
        if fast != None:
            slow = slow.next
        
        while slow and reversed_head:
            if slow.val != reversed_head.val:
                return False
            reversed_head = reversed_head.next
            slow = slow.next
        
        return True
