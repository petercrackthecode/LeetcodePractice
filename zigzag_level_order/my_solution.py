# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def group_nodes_by_level(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        ans = []

        have 2 queue: curr_level_nodes and next_level_nodes
        curr_levels_nodes = deque([root])
        while len(curr_levels_nodes) > 0 or len(next_level_nodes) > 0:
            curr_group = []
            while len(curr_levels_nodes) > 0:
            node = curr_levels_nodes.popleft()
            if node != None:
                curr_group.append(node.val)
                if node.left:
                next_level_nodes.append(node.left)
                if node.right:
                next_level_nodes.append(node.right)
            ans.append(curr_group)
            curr_levels_nodes = deque(next_level_nodes)
            next_level_nodes.clear()

        return ans

        Edges: E, Number of Nodes: V, height of tree is k
        Time: O(V+E)
        Space: O(2^(k-1))

        """
        ans = []
        curr_levels_nodes = deque([root])
        next_level_nodes = deque()
        while len(curr_levels_nodes) > 0 or len(next_level_nodes) > 0:
            curr_group = []
            while len(curr_levels_nodes) > 0:
                node = curr_levels_nodes.popleft()
                if node != None:
                    curr_group.append(node.val)
                    if node.left:
                        next_level_nodes.append(node.left)
                    if node.right:
                        next_level_nodes.append(node.right)
            ans.append(curr_group)
            curr_levels_nodes = deque(next_level_nodes)
            next_level_nodes.clear()
        return ans

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        bf_nodes = self.group_nodes_by_level(root)
        ans = []
        did_reverse = True

        for curr_nodes in bf_nodes:
            if not did_reverse:
                curr_nodes = list(reversed(curr_nodes))
            ans.append(curr_nodes)
            did_reverse = not did_reverse

        return ans
