from heapq import heappush, heappop, heapify
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        minHeap, maxHeap = [], []
        result = []

        for i in range(len(nums)):
            if not maxHeap or nums[i] <= -maxHeap[0]:
                heappush(maxHeap, -nums[i])
            else:
                heappush(minHeap, nums[i])

            # Balance heaps
            if len(maxHeap) > len(minHeap) + 1:
                heappush(minHeap, -heappop(maxHeap))
            if len(minHeap) > len(maxHeap):
                heappush(maxHeap, -heappop(minHeap))

            # Remove the element going out of the sliding window
            if i >= k:
                if nums[i-k] <= -maxHeap[0]:
                    maxHeap.remove(-nums[i-k])
                    heapify(maxHeap)
                else:
                    minHeap.remove(nums[i-k])
                    heapify(minHeap)

            # Balance heaps again after removal
            while len(maxHeap) > len(minHeap) + 1:
                heappush(minHeap, -heappop(maxHeap))
            while len(minHeap) > len(maxHeap):
                heappush(maxHeap, -heappop(minHeap))

            # Calculate median
            if i >= k-1:
                if k % 2 == 0:
                    result.append((-maxHeap[0] + minHeap[0]) / 2)
                else:
                    result.append(float(-maxHeap[0]))

        return result


nums: List[int] = [1, 3, -1, -3, 5, 3, 6, 7]
k: int = 3

# Expected: [1.00000,1.00000,1.00000]
print(f"Solution = {Solution().medianSlidingWindow(nums, k)}")
