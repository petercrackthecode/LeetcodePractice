# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def __init__(self):
        # Initiate the max_diameter as 1 since the number of nodes in the tree range [1, 10^4]
        self.max_diameter = 1

    def getHeightAndCalculateMaxDiameter(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_height = self.getHeightAndCalculateMaxDiameter(node.left)
        right_height = self.getHeightAndCalculateMaxDiameter(node.right)

        self.max_diameter = max(self.max_diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Steps to solve this problem:
        1. Traverse through every single node in the tree using depth-first search.
        2. For each node that makes a subtree, the diameter of that subtree is calculated as:
          diameter(node) = height(node.left) + height(node.right)
          Remember: the height of a tree (the number of vertices from the root node to the lowest
          node in the tree) is always 1 unit less than the number of edges that connect the root node
          to the lowest node in the tree, that's why we have the math above (the original math is
          diameter(node) = height(node.left) - 1 + height(node.right) - 1 + 1 + 1). The two plus-ones
          by the end of the equation represent two edges in the path to connect the left subtree
          & the right subtree to the root node.
        """
        # Edge cases: when we only have one node in the tree => doesn't qualify for the condition of
        # diameter: lenght of the longest path between any TWO NODES in a tree.
        if not root or (not root.left and not root.right):
            return 0

        self.getHeightAndCalculateMaxDiameter(root)

        return self.max_diameter
