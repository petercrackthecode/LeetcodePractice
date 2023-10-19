# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def __init__(self):
        self.is_node_found = False

    def find_path_to_target(self, node: 'TreeNode', target: 'TreeNode', path_so_far: List['TreeNode']) -> List['TreeNode']:
        if node.val == target.val:
            self.is_node_found = True
            return path_so_far

        if node.left != None:
            path_left = self.find_path_to_target(
                node.left, target, path_so_far + [node.left])
            if self.is_node_found:
                return path_left
        if node.right != None:
            return self.find_path_to_target(node.right, target, path_so_far + [node.right])

        return path_so_far

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        - Find the path to p from root. As we traverse through a node, add that node into a path list: path_so_far_p = []. Have a helper function called find_path_to_node(root: 'TreeNode', p: 'TreeNode') -> List['TreeNode']
        - Find the path to q from root. As we traverse As we traverse through a node, add that node into a path list: path_so_far_q = find_path_to_node(root, q)
        - i = 1. we'll use i to iterate through path_so_far_p & path_so_far_q
        path_so_far_p[0] = path_so_far_q[0]

        while i < min(len(path_so_far_p), len(path_so_far_q)) and path_so_far_p[i] == path_so_far_q[i]:
            i += 1

        return path_so_far_p[i - 1]

        N = number of nodes in the tree
        Time: O(N)
        Space: O(logN)
        -

        """
        self.is_node_found = False
        path_to_q = self.find_path_to_target(root, q, [root])
        self.is_node_found = False
        path_to_p = self.find_path_to_target(root, p, [root])

        i = 1
        shorter_path_length = min(len(path_to_p), len(path_to_q))

        while i < shorter_path_length and path_to_p[i].val == path_to_q[i].val:
            i += 1

        return path_to_p[i - 1]
