class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Second solution: 
        - counting sort, pass through the array one time, count the number of zeros, ones, and twos.
        - iterate through the array again, each time we iterate, if we still have zeroes, assign the current element to zero. Otherwise, we assign one, and otherwise two. Each time we assign an element to a value (zero, one, two), decrement the corresponding value within our track (until the point where the corresponding tracker's value is 0)
        """
        count_nums = [0, 0, 0]

        for num in nums:
            count_nums[num] += 1

        for i in range(len(nums)):
            if count_nums[0] > 0:
                nums[i] = 0
                count_nums[0] -= 1
            elif count_nums[1] > 0:
                nums[i] = 1
                count_nums[1] -= 1
            else:  # 2
                nums[i] = 2
                count_nums[2] -= 1
