# https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.is_bst_still_valid = True

    def is_valid_bst_helper(self, node: Optional[TreeNode], left_bound: int, right_bound: int) -> None:
        if not node:
            return
        if not (left_bound < node.val and node.val < right_bound):
            self.is_bst_still_valid = False
            return

        new_right_bound_for_left_node = node.val
        self.is_valid_bst_helper(node.left, left_bound,
                                 new_right_bound_for_left_node)
        if self.is_bst_still_valid:
            new_left_bound_for_right_node = node.val
            self.is_valid_bst_helper(
                node.right, new_left_bound_for_right_node, right_bound)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Logic of a binary tree:
        - Every node on the left side of a node is smaller than that node.
        - Every node on the right side of a node is greater than that node.
        => We have to save the left and right boundaries to keep track of the rule above.
        - Have a class variable called self.is_bst_still_valid to keep track of the global condition above.
        - When one node in the tree falsifies the condition, change self.is_bst_still_valid = False.
        - Because we only need one node that violates the above condition to make the BST invalid, 
        at the beginning of self.isValidBST, always check if self.is_bst_still_valid == True to ensure that there is
        no other node in the tree that is invalid and it's worth checking the current node. 
        - Have a helper function called is_valid_bst_helper(self, node, left_bound, right_bound) to save the left_bound
        and right_bound for our current node check.
        - Before we go right, change the left_boundary = current_node.val
        - Before we go left, change the right_boundary = current_node.val
        - if not (left_boundary < current_node.val and current_node.val < right_boundary):
            self.is_bst_still_valid = False
            return
          else:
            new_right_bound_for_left_node = current.val
            self.is_bst_still_valid(current_node.left, left_bound, new_right_bound_for_left_node)
            new_left_bound_for_right_node = current.val
            self.is_bst_still_valid(current_node.right, new_left_bound_for_right_node, right_bound)
        """
        if root:
            left_bound_for_left_node = float('-inf')
            right_bound_for_left_node = root.val
            left_bound_for_right_node = root.val
            right_bound_for_right_node = float('+inf')
            # check left node
            self.is_valid_bst_helper(
                root.left, left_bound_for_left_node, right_bound_for_left_node)
            if self.is_bst_still_valid:
                self.is_valid_bst_helper(
                    root.right, left_bound_for_right_node, right_bound_for_right_node)

        return self.is_bst_still_valid
