from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindromic_array(arr: List[int]) -> bool:
    if len(arr) <= 1:
        return True
    left, right = (0, len(arr) - 1)
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        + Parse all elements in the linked list to an array.
        + Check if the array is a palindrome
        """
        numbers = []
        temp = head
        while temp:
            numbers.append(temp.val)
            temp = temp.next
        return is_palindromic_array(numbers)
