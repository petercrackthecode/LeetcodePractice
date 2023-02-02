# https://leetcode.com/problems/pancake-sorting/
from typing import List, Dict
import heapq

class Solution:
    def flip(self, arr: List[int], k: int, element_index_lookup: Dict[int, int]) -> None:
        [left, right] = [0, k]
        while left < right:
          element_index_lookup[arr[left]], element_index_lookup[arr[right]] = right, left
          arr[left], arr[right] = arr[right], arr[left]
          left += 1
          right -= 1

    def pancakeSort(self, arr: List[int]) -> List[int]:
        """
        + Have a max_heap arr: max_heap = list(arr)
        + Convert max_heap from a normal list into a max heap: heapq.heapify(arr)
        + Have a dictionary called element_index_lookup:
          - key: the value of the element.
          - value: the index of the element.
        + ans = []
        + Have a while loop as long as len(max_heap) > 1:
          - current_max = heapq.heappop(max_heap)
          - ans.append(element_index_lookup[current_max] + 1)
          - self.flip(arr, element_index_lookup[current_max])
          - ans.append(len(max_heap) + 1)
          - self.flip(arr, len(max_heap), element_index_lookup)
        + Return ans
        """
        ans = []

        max_heap = [-num for num in arr]
        heapq.heapify(max_heap)
        element_index_lookup = dict()
        for (index, num) in enumerate(arr):
          element_index_lookup[num] = index
        while len(max_heap) > 1:
          current_max = -heapq.heappop(max_heap)
          ans.append(element_index_lookup[current_max] + 1)
          self.flip(arr, element_index_lookup[current_max], element_index_lookup)

          ans.append(len(max_heap) + 1)
          self.flip(arr, len(max_heap), element_index_lookup)

        return ans