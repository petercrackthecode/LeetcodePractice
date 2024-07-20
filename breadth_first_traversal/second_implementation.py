from typing import List, Optional, Deque
from collections import deque
import unittest


class Node:
    def __init__(
        self, val: int, left: Optional["Node"] = None, right: Optional["Node"] = None
    ):
        self.val: int = val
        self.left: Optional["Node"] = left
        self.right: Optional["Node"] = right


def breadth_first_traversal(root: Optional["Node"]):
    """
    - given the root node, return the list of values in the breadth first traversal order of the tree
    - traversal order: left -> right
    """
    ans: int = []

    # have a deque functioning as a queue to save the unvisited nodes
    unvisited_nodes: Deque[Optional["Node"]] = deque([root])

    while len(unvisited_nodes) > 0:
        popped: Optional["Node"] = unvisited_nodes.popleft()
        if not popped:
            continue
        # non-empty node -> add popped's val to ans
        ans.append(popped.val)
        # add the left & right children of popped to our queue
        unvisited_nodes.append(popped.left)
        unvisited_nodes.append(popped.right)

    return ans
