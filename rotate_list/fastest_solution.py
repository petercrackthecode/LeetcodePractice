"""
Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
"""
class Solution:
	def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		if not head or not head.next:
			return head

		linkedList_len = 1
		lastElement = head

		while lastElement.next:
			lastElement = lastElement.next
			linkedList_len += 1

		lastElement.next = head

		reminder = k % linkedList_len

		tempNode = head

		for _ in range(linkedList_len - 1 - reminder):
			tempNode = tempNode.next

		answer = tempNode.next
		tempNode.next = None

		return answer