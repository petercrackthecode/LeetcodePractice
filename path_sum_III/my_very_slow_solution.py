
# https://leetcode.com/problems/path-sum-iii
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0
        self.node_started_from = set()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        - From the root node, travel down to its left and right children. Calculate the sum of each path as we go, then call the function again until we reach a null node. Let's call the function that does this task calculate_sums_of_path_started_from_current_node(node, curr_sum)
        - Have a set called self.node_started_from to save all the node that we already started the path from, so we won't go through them again.
        - As we traverse through, calculate the current sum of the current_path, and if current_sum == target_sum:
            self.ans += 1
        - Within the above function, also call the calculate_sums_of_path_started_from_current_node function again for the left child and the right child of the current node
        - In the end, return ans
        """
        def calculate_sums_of_path_started_from_current_node(node: Optional[TreeNode], curr_sum: int) -> None:
            if not node:
                return

            curr_sum += node.val
            if curr_sum == targetSum:
                self.ans += 1

            # calculate the sums of path starting from node.left or node.right
            if node.left and not node.left in self.node_started_from:
                self.node_started_from.add(node.left)
                calculate_sums_of_path_started_from_current_node(node.left, 0)
            if node.right and not node.right in self.node_started_from:
                self.node_started_from.add(node.right)
                calculate_sums_of_path_started_from_current_node(node.right, 0)

            calculate_sums_of_path_started_from_current_node(
                node.left, curr_sum)
            calculate_sums_of_path_started_from_current_node(
                node.right, curr_sum)
        self.node_started_from.add(root)
        calculate_sums_of_path_started_from_current_node(root, 0)
        return self.ans
