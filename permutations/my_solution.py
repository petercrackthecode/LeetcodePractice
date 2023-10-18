from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        nums = [1,2,3]
        output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        - iterate through position 0..len(nums)-1: each time we iterate through an element, take that number to our permutation. 
            [2, 3]
            permu[0] = [1, 2, 3]
            permu[1] = [1, 3, 2]
            permute([2, 3]) = [[2, 3], [3, 2]]

          if len(nums) <= 1:
              return nums
          ans = []
        - pick a number from nums, exclude that number from nums:
            for (idx, num) in enumerate(nums):
                remaining_nums = nums[0:idx] + nums[idx+1:]
                sub_permu = permute(remaining_nums)
                for permu in sub_permu:
                    ans.append([num] + permu)

        - return ans

        N = len(nums)
        Time: O(N!)
        Space: O(N^2)
        """
        if len(nums) <= 1:
            return [nums]

        ans = []

        for (idx, num) in enumerate(nums):
            remaining_nums = nums[0:idx] + nums[idx+1:]
            sub_permu = self.permute(remaining_nums)
            for permu in sub_permu:
                ans.append([num] + permu)

        return ans
