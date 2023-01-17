# https://leetcode.com/problems/binary-tree-level-order-traversal

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes_queue = deque()
        nodes_queue.append((root, 1))
        grouped_nodes_values = []

        while len(nodes_queue) > 0:
            (node, level) = nodes_queue.popleft()
            if not node:
                continue

            while len(grouped_nodes_values) < level:
                grouped_nodes_values.append([])
            grouped_nodes_values[level-1].append(node.val)

            if node.left:
                nodes_queue.append((node.left, level + 1))
            if node.right:
                nodes_queue.append((node.right, level + 1))

        return grouped_nodes_values
