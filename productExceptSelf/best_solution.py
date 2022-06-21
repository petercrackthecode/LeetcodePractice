# https://leetcode.com/problems/product-of-array-except-self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        left: int = 1
        right: int = 1

        l_index = 0
        r_index = array_length - 1

        answer = [1] * array_length
        while l_index < array_length or r_index >= 0:
            if l_index > 0:
                left *= nums[l_index - 1]
            if r_index < array_length - 1:
                right *= nums[r_index + 1]
            answer[l_index] *= left
            answer[r_index] *= right

            l_index += 1
            r_index -= 1

        return answer
