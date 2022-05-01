class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:

"""
There are 2 actions we gotta do at this step:
1. Mark elements as duplicated.
2. Interate through the array. 
   For every duplicate element, swap them with the next non-duplicate element.
"""
