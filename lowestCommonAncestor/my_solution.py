from collections import deque
from lib2to3.pytree import Node

# Definition for a binary tree node.
# Class TreeNode:
# def __init__(self, x):
#   self.val = x
#   self.left = None
#   self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: "TreeNode", q: "TreeNode") -> "TreeNode":
        """
        Let's say we have two nodes p and q that we gotta find the lowest common ancestor to.
        1. Find the path to node p. Save it inot a deque called p_path
        2. Find the path to node q. Save it into a deque called q_path
        3. Since the beginning of both deques, find the longest common path between p_path and q_path. Let's call it C.
        4. Return the last element of C.
        """

        # Given a root node and a node to find.
        # Return the deque of all the nodes that form that path from the root node to that to-be-found node
        def getPathToNode(root: 'TreeNode', nodeToFind: 'TreeNode'):
            if not root or not nodeToFind:
                return None

            path = deque([root])
            while root and root != nodeToFind:
                if root.val < nodeToFind.val:
                    root = root.right
                else:
                    root = root.left
                if root:
                    path.append(root)

            return path

        p_path = getPathToNode(root, p)
        q_path = getPathToNode(root, q)

        ans = None
        while q_path and p_path and q_path[0] == p_path[0]:
            ans = p_path[0]
            p_path.popleft()
            q_path.popleft()

        return ans
