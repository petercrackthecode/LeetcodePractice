from collections import deque
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        + We should calculate the width of each level.
        + Return the max of all the widths.

        We should know how many nodes are possibly there at a level.
        + Breadth first traversal.
        + Take the temp node initially assigned as the root node, continuously extracting the child of the temp node to a queue.
        + Until the queue's length is 0, keep extracting the children of the nodes from the queue.
        + When you extract a node from its parent, if the node is the left child, position = parent's position * 2 - 1. Else, right child's position = parent's position * 2. 
        + Then, compare it to the local_max_width and local_min_width as:
            local_max_width = max(local_max_width, node_index)
            local_min_width = min(local_min_width, node_index)
        + By the end of each queue iteration, compare the subtraction of local_max_width to local_min_width to max_width:
            max_width = max(max_width, local_max_width - local_min_width + 1)

        + save a tuple to the queue: (node, position)
        + By default, the root node has the position 1.
        """
        q = deque([(root, 1)])
        max_width = 1

        while len(q) > 0:
            temp_q = deque()
            local_max_width = float('-inf')
            local_min_width = float('+inf')

            for (node, position) in q:
                local_max_width = max(local_max_width, position)
                local_min_width = min(local_min_width, position)
                if node.left:
                    temp_q.append((node.left, position * 2 - 1))
                if node.right:
                    temp_q.append((node.right, position * 2))
            max_width = max(max_width, local_max_width - local_min_width + 1)
            q.clear()
            q = temp_q

        return max_width
