from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # since 1 <= nums's length <= 5000, this linear search operation is possible.
        return target in nums
