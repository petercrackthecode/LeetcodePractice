from typing import List


class TreeNode:
    def __init__(self, _key: str = "", _val: int = 0, _children: List[TreeNode] = None):
        self.key = _key
        self.val = _val
        self.children = _children
