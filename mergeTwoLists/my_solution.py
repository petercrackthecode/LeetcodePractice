# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        ans = temp
        
        while l1 and l2:
            if l1.val <= l2.val:
                if not temp:
                    temp = ListNode(l1.val)
                    ans = temp
                else:
                    temp.next = ListNode(l1.val)
                    temp = temp.next
                l1 = l1.next
            else:
                if not temp:
                    temp = ListNode(l2.val)
                    ans = temp
                else:
                    temp.next = ListNode(l2.val)
                    temp = temp.next
                l2 = l2.next
        
        while l1:
            if not temp:
                return l1
            else:
                temp.next = ListNode(l1.val)
                temp = temp.next
            l1 = l1.next
        
        while l2:
            if not temp:
                return l2
            else:
                temp.next = ListNode(l2.val)
                temp = temp.next
            l2 = l2.next
        
        return ans
        
        