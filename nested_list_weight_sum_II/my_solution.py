# https://leetcode.com/problems/nested-list-weight-sum-ii/description/
from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        """
                            1
        nestedList = [[1,1],2,[1,1]]
        ans        = 8
        weight = maxDepth - (the depth of the integer) + 1
        return sum of each integer multiplied by its weight

        to calculate the weight, we'll need the max_depth, the integer's depth and its value
        a nestedInteger can only hold one list
        a nestedInteger can only hold one integer

        - assuming that the depth level starts from 1, and increments by 1 everytime we enter a list
        - find the max_depth: have a helper function called get_max_depth(nestedList: List[NestedInteger]): max_depth:int = get_max_depth(nestedList)
        - have a helper function called get_list_weight(nestedList: List[NestedInteger], curr_depth: int). get_list_weight should be able to access the max_depth.
        - return get_list_weight(nestedList, 1)
        """
        max_depth: int = 1

        def get_max_depth_helper(nested_int: NestedInteger, curr_depth: int) -> int:
            nonlocal max_depth
            max_depth = max(max_depth, curr_depth)
            # [[1,1],2,[1,1]]
            possible_nested_list: Optional[List[NestedInteger]] = nested_int.getList()
            if (
                possible_nested_list != None
            ):  # we have a nested list => recursively iterating thru the nested integers in the list on a deeper depth (curr_depth + 1)
                for inner_nested_int in possible_nested_list:
                    get_max_depth_helper(inner_nested_int, curr_depth + 1)

        for nested_int in nestedList:
            get_max_depth_helper(nested_int, 1)

        def get_list_weight(nestedList: List[NestedInteger], curr_depth: int) -> int:
            # integer's weight = maxDepth - (integer's curr_depth) + 1
            # integer's units = integer's value * integer's weight
            nonlocal max_depth
            ans: int = 0
            for nested_int in nestedList:
                if nested_int.isInteger():
                    nest_int_val: int = nested_int.getInteger()
                    weight: int = max_depth - curr_depth + 1
                    ans += nest_int_val * weight
                else:  # nested_int is a List[NestedInteger]
                    ans += get_list_weight(nested_int.getList(), curr_depth + 1)

            return ans

        return get_list_weight(nestedList, 1)
