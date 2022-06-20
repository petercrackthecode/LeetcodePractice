# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        didNumberExist = dict()

        for num in nums:
            if num in didNumberExist:
                return True
            didNumberExist[num] = True

        return False
