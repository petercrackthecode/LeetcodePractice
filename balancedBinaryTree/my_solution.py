from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.is_tree_balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        1. From the root node, recursively traverse to every single node in the tree.
        2. While we traversing, calculate the height of each node with this algorithm:
            height(node) = max(height(node.left), height(node.right)) + 1
            Also, every time we do that, we can check if the height if node.left and node.right differ by
            more than 1: abs(height(node.left) - height(node.right)) > 1.
            If so, return false immediately: is_tree_balanced = false.
            Otherwise, keep traversing until facing an empty node.
            Base case: height(emptyNode) = 0.

            have a variable called is_tree_balanced = true.
            if is_tree_balanced is every be false, stop the recursive callstack and return False immediately.
        """

        def height(node: Optional[TreeNode]) -> int:
            if not self.is_tree_balanced:
                return 0

            if not node:
                return 0
            else:
                left_child_height = height(node.left)
                right_child_height = height(node.right)
                if abs(left_child_height - right_child_height) > 1:
                    self.is_tree_balanced = False
                    return 0

                return 1 + max(left_child_height, right_child_height)

        height(root)

        return self.is_tree_balanced
