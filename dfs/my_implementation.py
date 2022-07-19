from typing import Optional


class BinaryTree:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def depthFirstSearch(node: Optional[BinaryTree]) -> None:
    if not node:
        return

    print(node.val, end=" ")
    depthFirstSearch(node.left)
    depthFirstSearch(node.right)


node = BinaryTree(1)
node.left = BinaryTree(2)
node.right = BinaryTree(3)
node.left.left = BinaryTree(4)
node.left.right = BinaryTree(5)
node.right.left = BinaryTree(6)
node.right.right = BinaryTree(7)

depthFirstSearch(node)
