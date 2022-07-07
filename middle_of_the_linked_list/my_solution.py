# https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        list_length = 0

        while temp:
            list_length += 1
            temp = temp.next

        steps_to_get_to_middle_node_from_head = list_length // 2

        ans = head
        while steps_to_get_to_middle_node_from_head > 0:
            ans = ans.next
            steps_to_get_to_middle_node_from_head -= 1

        return ans
