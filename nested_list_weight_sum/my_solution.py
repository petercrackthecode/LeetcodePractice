# https://leetcode.com/problems/nested-list-weight-sum/
from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
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
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        '''
        [[1,1],2,[1,1]]
        output = 10 | 1 * 2 + 1 * 2 + 2 * 1 + 1 * 2 + 1 * 2 = 2 + 2 + 2 + 2 + 2 = 10
        depth of num: number of list it is inside of.

        [1, [4, [6]]]
        output = 27 | 1*1 + 4*2 + 6*3 = 1 + 8 + 18 = 27

        - have a variable called ans:int = 0
        - have a helper function called get_nested_int_sum(nested_int: NestedInteger) -> int to recursively loop thru every element within the nested_int and calculate the sum of the entire nested_int.
        - loop: for each nested_int within nestedList:
            - increment ans by get_nested_int_sum(nested_int)
        - return ans
        '''
        ans:int = 0
        
        def get_nested_int_sum(nested_int: NestedInteger, curr_level: int) -> int:
            if nested_int.isInteger():
                return curr_level * nested_int.getInteger()
            else: # not an integer => nested_int contain a list of NestedInteger -> loop thru every nested integer within nested_int.getList() and call get_nested_int_sum(curr_level+1) on each of 'em
                ans:int = 0
                for inner_nested_int in nested_int.getList():
                    ans += get_nested_int_sum(inner_nested_int, curr_level+1)

                return ans

        for nested_int in nestedList:
            ans += get_nested_int_sum(nested_int, 1)

        return ans