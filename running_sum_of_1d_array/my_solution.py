# link: https://leetcode.com/problems/running-sum-of-1d-array/submissions/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        running_sum_at_i = 0
        for num in nums:
            running_sum_at_i += num
            ans.append(running_sum_at_i)
        
        return ans
        
    """
    Good rules of thumb for the first step before answering a coding interview question:
    1. Ask for the function: What's the input, what's the output (How many parameters does the function take? What's the return type of the function)
    2. Ask if you have to validate the input (what's the type of the parameters, do we need to verify if they match those type? Can the input be a null value (undefined, null, None, NaN)?)
    3. How do we know if our function works? If we have to write test cases, can you provide some expected results? How do you compare the expected results and your function's output?
    """