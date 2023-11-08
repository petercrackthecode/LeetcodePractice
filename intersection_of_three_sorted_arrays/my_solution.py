# https://leetcode.com/problems/intersection-of-three-sorted-arrays/
from typing import List


class Solution:
    def has_target(self, nums: List[int], target: int) -> bool:
        [left, right] = [0, len(nums) - 1]
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """
        - get the array with the shortest length within arr1, arr2, arr3 and assign it to shortest_arr
        - iterate through shortest_arr. For each element, search if they both exist in the other array using binary search. If it exists in both, add the element to our ans array.
        """
        ans = []
        len_1 = len(arr1)
        len_2 = len(arr2)
        len_3 = len(arr3)

        shortest_arr = arr1 if len_1 == min(
            len_1, len_2, len_3) else arr2 if len_2 < len_3 else arr3
        other_1 = []
        other_2 = []

        if shortest_arr == arr1:
            other_1 = arr2
            other_2 = arr3
        elif shortest_arr == arr2:
            other_1 = arr1
            other_2 = arr3
        else:
            other_1 = arr1
            other_2 = arr2

        for elem in shortest_arr:
            if self.has_target(other_1, elem) and self.has_target(other_2, elem):
                ans.append(elem)

        return ans
