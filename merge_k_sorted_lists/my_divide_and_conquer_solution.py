# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional["ListNode"]]) -> Optional["ListNode"]:
        '''
        - Since our task involves multiple lists, we can use the divide and conquer technique, starting
        with pairing the lists and then merging each pair. We repeat this until all the given lists are merged.
        This way, after the first pairing, we're left with k/2 lists, then (k/4), (k/8) and so on.
        '''
        #           0       1       2
        # lists = [[1,4,5],[1,3,4],[2,6]]
        def merge_2_sorted_lists(lst_1: Optional["ListNode"], lst_2: Optional["ListNode"]) -> Optional["ListNode"]:
            if not lst_1:
                return lst_2
            if not lst_2:
                return lst_1
            
            temp_1:Optional["ListNode"] = lst_1
            temp_2:Optional["ListNode"] = lst_2

            ans:Optional["ListNode"] = None
            ans_tail:Optional["ListNode"] = None

            def add_to_ans(val: int) -> None:
                nonlocal ans, ans_tail
                if not ans:
                    ans = ListNode(val)
                    ans_tail = ans
                else:
                    ans_tail.next = ListNode(val)
                    ans_tail = ans_tail.next

            while temp_1 and temp_2:
                if temp_1.val <= temp_2.val:
                    add_to_ans(temp_1.val)
                    temp_1 = temp_1.next
                else:
                    add_to_ans(temp_2.val)
                    temp_2 = temp_2.next

            while temp_1:
                add_to_ans(temp_1.val)
                temp_1 = temp_1.next

            while temp_2:
                add_to_ans(temp_2.val)
                temp_2 = temp_2.next

            return ans

        def merge_sorted_list_within_range(start: int, end: int) -> Optional["ListNode"]:
            nonlocal lists
            '''
            '''
            if end - start < 0:
                return None
            elif end - start == 0:
                return lists[start]
            elif end - start == 1:
                return merge_2_sorted_lists(lists[start], lists[end])
            else: # more than 2 lists -> divide and conquer
                mid: int = (end - start) // 2 + start
                list_from_left_range:Optional["ListNode"] = merge_sorted_list_within_range(start, mid)
                list_from_right_range:Optional["ListNode"] = merge_sorted_list_within_range(mid+1, end)

                return merge_2_sorted_lists(list_from_left_range, list_from_right_range)


        return merge_sorted_list_within_range(0, len(lists) - 1)