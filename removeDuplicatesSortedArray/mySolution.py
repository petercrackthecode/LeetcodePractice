class Solution:
    # mark the duplicate elements in a sorted array and return the duplicates count
    def markDuplicates(self, nums: List[int]) -> int:
        dupCount = 0
        for i in range(len(nums)):
            if nums[i] == nums[i +1]:
                # Mark the element as duplicate by assigning an out-of-range value to it: -101
                nums[i] = -101
                dupCount = dupCount + 1
        return dupCount
                
    def swapTwoArrayElements(self, arr: List[int], x: int, y: int) -> None:
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp
        
    def removeDuplicates(self, nums: List[int]) -> int:
        # Mark elements as duplicated.
        dupCount = self.markDuplicates(nums)
        
        if dupCount == 0:
            # No duplicates found. Return the array's length immediately.
            return len(nums)
        
        # Iterate through the array to swap duplicate elements to the array's tail.
        duplicateEleIndex = -1
        for i in range(len(nums)):
            if nums[i] != 101 and duplicateEleIndex != -1:
                swap(nums, duplicateEleIndex, i)
                duplicateEleIndex = duplicateEleIndex + 1
                while d
        
        
"""
There are 2 actions we gotta do to solve the problem:
1. Mark elements as duplicated.
2. Interate through the array. 
   For every duplicate element, swap them with the next non-duplicate element.
"""