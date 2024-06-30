# https://leetcode.com/problems/path-sum-iii/
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional["TreeNode"], targetSum: int) -> int:
        '''
        - number of paths where each path's sum is targetSum
        
                                    
                                    10
                                /       \
                              5          -3
                            /  \            \
                           3-A   2           11
                         /  \     \
                        3-B   -2    1
                        
        - targetSum = 8
        
        3-A:
        {
            [3A]: 3
            [3A, 3B]: 6,
            [3A, -2]: 1
        }
        
        2: {
            [2]: 2
            [2, 1]: 3
        }
        
        5: {
            [5, 3A]: 8,
            [5, 3A, 3B]: 11,
            [5, 3A, -2]: 6,
            [5, 2]: 7
            [5, 2, 1]: 8
        }
        
        - given a node, return the sums of each path we can form from that node: path_sums_lookup:DefaultDict[Optional[TreeNode], List[int]] = defaultdict(list)
        - ans:int = 0
        - starting from root:
            - if root.val equals targetSum: increment ans by 1
            - get the path_sum_left = get_path_sum(root.left)
            - get the path_sum_right = get_path_sum(root.right)
            - loop: for sum in path_sum_left:
                - if sum plus root.val equals targetSum: increment ans by 1
            - loop: for sum in path_sum_right:
                - if sum plus root.val equals targetSum: increment ans by 1
                
        - Apply the same logic above down to every single node: calc_path_sum(node: Optional[TreeNode])
        '''
        ans:int = 0
        
        def get_path_sum(node:Optional["TreeNode"]) -> List[int]:
            nonlocal ans, targetSum
            
            # if not node:
            #     print("empty\n")
            # else:
            #     print(f"{node.val}\n")
            
            if not node:
                return []

            # path sums are the sums of all paths can be created from the curr node
            path_sums:List[int] = [node.val]
            
            if node.val == targetSum:
                ans += 1
                
            path_sums_left:List[int] = get_path_sum(node.left)
            path_sums_right:List[int] = get_path_sum(node.right)
                
            for _sum in path_sums_left:
                path_sums.append(node.val + _sum)
                if _sum + node.val == targetSum:
                    ans += 1
            
            for _sum in path_sums_right:
                path_sums.append(node.val + _sum)
                if _sum + node.val == targetSum:
                    ans += 1
            
            return path_sums
        
        get_path_sum(root)
        
        return ans
        
        