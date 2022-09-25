# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_to_list(node: Optional[TreeNode], nums: List[int]) -> None:
    if not node:
        return
    bst_to_list(node.left, nums)
    nums.append(node.val)
    bst_to_list(node.right, nums)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        bst_to_list(root, nums)

        return nums[k-1]
