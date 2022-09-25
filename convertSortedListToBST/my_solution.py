# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_bst_helper(nums: List[int], left: int, right: int) -> Optional[TreeNode]:
    mid = (right - left) // 2 + left
    root = TreeNode(nums[mid])
    if mid > left:
        root.left = array_to_bst_helper(nums, left, mid-1)
    if mid < right:
        root.right = array_to_bst_helper(nums, mid+1, right)

    return root


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        if mid > 0:
            root.left = array_to_bst_helper(nums, 0, mid-1)
        if mid < len(nums) - 1:
            root.right = array_to_bst_helper(nums, mid+1, len(nums) - 1)

        return root
