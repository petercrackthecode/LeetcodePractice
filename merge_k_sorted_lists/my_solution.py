# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import Optional, List, Tuple
from heapq import heapify, heappop, heappush
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional["ListNode"]]) -> Optional["ListNode"]:
        ans:Optional["ListNode"] = None
        ans_tail:Optional["ListNode"] = ans
        linked_list_vals_asc:List[Tuple[int, int]] = []

        def add_new_node_to_ans(val: int) -> None:
            nonlocal ans, ans_tail
            if not ans:
                ans = ListNode(val, None)
                ans_tail = ans
            else:
                ans_tail.next = ListNode(val, None)
                ans_tail = ans_tail.next

        for i, linked_list in enumerate(lists):
            if not linked_list:
                # empty list
                continue
            val:int = linked_list.val
            linked_list_vals_asc.append((val, i))

        heapify(linked_list_vals_asc)

        while len(linked_list_vals_asc) > 0:
            val, idx = heappop(linked_list_vals_asc)
            add_new_node_to_ans(val)

            lists[idx] = lists[idx].next
            
            if lists[idx]:
                # push (lists[idx].val, idx) back to our heap
                heappush(linked_list_vals_asc, (lists[idx].val, idx))

        return ans