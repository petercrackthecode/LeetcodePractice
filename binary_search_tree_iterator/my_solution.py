# https://leetcode.com/problems/binary-search-tree-iterator/
from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_to_list(node: Optional[TreeNode], nums: List[int]) -> None:
    if not node:
        return
    bst_to_list(node.left, nums)
    nums.append(node.val)
    bst_to_list(node.right, nums)


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nums = []
        bst_to_list(root, self.nums)
        self.curr_index = -1

    def next(self) -> int:
        self.curr_index += 1
        return self.nums[self.curr_index]

    def hasNext(self) -> bool:
        return self.curr_index < len(self.nums) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
