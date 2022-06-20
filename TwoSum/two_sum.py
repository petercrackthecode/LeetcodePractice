# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. Have a dictionary, where:
           - The keys are the value of the elements in the array.
           - The values are the indices of the elements. If there're two elements that share the same value, only save the index of the first appeared one.
        2. Scan through the array to initiate the dictionary.
        3. Scan through the array one more time. If the subtraction of target and the current element's value matches a key in the dictionary and the current element's index is different from the dictionary's value at that key (so it represents a different element in the array), returns a pair [dictionary[key], element's index].
        """
        remainders_and_indices = dict()
        for index in range(len(nums)):
            remainder = target - nums[index]
            if remainder in remainders_and_indices and index != remainders_and_indices[remainder]:
                return [remainders_and_indices[remainder], index]
            remainders_and_indices[nums[index]] = index

        return [-1, -1]
