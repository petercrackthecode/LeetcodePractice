class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        leftMultiply = [1] * array_length
        rightMultiply = [1] * array_length
        # Initialize the leftMultiply array
        for index, num in enumerate(nums):
            # ignore the first element in leftMultiply since its value will be 1
            if index > 0:
                leftMultiply[index] = leftMultiply[index - 1] * nums[index - 1]
        # Initialize the rightMultiply array
        for index in reversed(range(array_length)):
            # ignore the last element in rightMultiply since its value will be 1
            if index < array_length - 1:
                rightMultiply[index] = rightMultiply[index + 1] * \
                    nums[index + 1]

        answer = []
        for index in range(len(nums)):
            answer.append(leftMultiply[index] * rightMultiply[index])

        return answer
