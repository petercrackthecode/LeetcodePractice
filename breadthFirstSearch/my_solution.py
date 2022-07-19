# Given the rootnode of a tree, print all the nodes from the tree using
# breadth-first traversal
from collections import deque
from typing import Optional


class BinaryTree:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def breadthFirstTraversal(node: Optional[BinaryTree]) -> None:
    if not node:
        return

    same_level_nodes = deque()
    same_level_nodes.append(node)
    temp = None

    while len(same_level_nodes) > 0:
        temp = same_level_nodes.popleft()
        if temp:
            print(temp.val, end=" ")
        if temp.left:
            same_level_nodes.append(temp.left)
        if temp.right:
            same_level_nodes.append(temp.right)

    return


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

breadthFirstTraversal(root)
