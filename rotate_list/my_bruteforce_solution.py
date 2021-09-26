# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def countNodes(self, head: Optional[ListNode]) -> int:
        ans = 0
        
        while head:
            ans = ans + 1
            head = head.next
        
        return ans
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        n = self.countNodes(head)
        
        # only rotate (k % n) times to avoid repetitive rotations
        k = k % n
        
        # if we rotate a list (m * n) times the list remains the same
        if k == 0:
            return head
        
        nodes_traversed_before_rotation = n - k - 1
        temp = head
        
        while nodes_traversed_before_rotation > 0:
            temp = temp.next
            nodes_traversed_before_rotation = nodes_traversed_before_rotation - 1
        
        rotatedNode = temp.next
        ans = rotatedNode
        temp.next = None
        
        while rotatedNode and rotatedNode.next != None:
            rotatedNode = rotatedNode.next
        rotatedNode.next = head
        
        return ans