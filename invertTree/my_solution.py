from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursively swap the children before swaping the parents.

        # Ignore the case where the the current node is empty or doesn't have any left or right child node to swap.
        if (not root):
            return None

        if root.left or root.right:
            self.invertTree(root.left)
            self.invertTree(root.right)

            root.left, root.right = root.right, root.left

        return root
