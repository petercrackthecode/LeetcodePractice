# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        one valid solution
        O(1) space
        numbers is sorted non-decreasingly
        return List[int] with two elements index1 and index2,
        where index1 < index2
                        <-  r
                   l ->
                   0  1  2  3
        numbers = [1, 2, 3, 4]
        target = 3
        output = [1, 2]

        - l = 0, r = len(numbers)
        - sum = numbers[0] + numbers[3] = 5 > 3 (target) => reduce our sum

        /////////////////////////

        - l = 0, r = len(numbers) - 1
        - loop: while l < r:
            - sum:int = numbers[l] + numbers[r]
            - if sum equals target: return [l+1, r+1]
            - otherwise, if sum > target: 
                - decrement right by 1 (if we already have a smaller sum, then 
                we've already reached it by l)
            - otherwise, if sum < target:
                - increment left by 1 (if we already have a bigger sum, then we've
                already reached it by r)

        - return [0, 0]
        '''
        left:int = 0
        right:int = len(numbers)-1

        while left < right:
            _sum:int = numbers[left] + numbers[right]
            if _sum == target:
                return [left+1, right+1]
            elif _sum > target:
                right -= 1
            else: # _sum < target
                left += 1

        return [0, 0]