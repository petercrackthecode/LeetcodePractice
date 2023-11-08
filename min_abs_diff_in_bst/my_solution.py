# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.last_visited = -(10**5 + 1)
        self.ans = float('inf')

    def inorder_traverse(self, node: Optional[TreeNode]) -> None:
        if not node:
            return

        self.inorder_traverse(node.left)

        last_gap = node.val - self.last_visited
        self.ans = min(self.ans, last_gap)
        self.last_visited = node.val

        self.inorder_traverse(node.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        inorderly traverse through our tree, have a variable called last_visited to save the last visited node's value. Then, each time we visit a new node, take the subtraction between the curr_node.val and last_visited, and compare and assign to ans: ans = min(ans, curr_node.val - last_visited)
        """
        self.inorder_traverse(root)

        return self.ans
