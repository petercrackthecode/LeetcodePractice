# https://leetcode.com/problems/sort-list/
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numbers = []
        temp = head
        while temp:
            numbers.append(temp.val)
            temp = temp.next
        sorted_numbers = sorted(numbers)
        temp = head
        i = 0
        while i < len(sorted_numbers) and temp:
            temp.val = sorted_numbers[i]
            temp = temp.next
            i += 1

        return head
