"""
Definition for singly-linked list.
class ListNode:
	def ___init___(self, val=0, next=None):
		self.val = val
		self.next = next
"""
class Solution:
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if head and head.next:
			ret, ptr, pre = head.next, head, None

			while ptr:
				if not ptr.next:
					break
				ptr.next, ptr, ptr.next = ptr.next.next, ptr.next, ptr

				if pre:
					pre.next = ptr

				pre, ptr = ptr.next, ptr.next.next
			return ret
		else:
			return head