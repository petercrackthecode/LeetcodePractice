# https://www.geeksforgeeks.org/quickselect-algorithm/
from typing import List

# Standard partition process of quickSort()
# It considers the last element as pivot, and moves all smaller elements to the left of it & greater elements to the right
def partition(arr:List[int], left:int, right:int) -> int:
  '''
   l
            r
         j
   i
  [3, 5, 2, 1]
   0  1  2  3

  x = 1
  arr[j] = 3

  eventually, swap arr[0] (i=0) with arr[3] (r=3), we have: [1, 5, 2, 3]

   l
               r
            j
      i
  [2, 3, 9, 5, 4]
   0  1  2  3  4

  x = 4
  arr[j] = 3
  '''
  pivot_val:int = arr[right]
  pivot_idx:int = left
  
  for i in range(left, right): # j = l -> r-1
    # i will always reside at the index where arr[i] > arr[r] (our pivot)
    # i will only increment when we find an index j where arr[j] <= pivot_val
    if arr[i] <= pivot_val:
      arr[pivot_idx], arr[i] = arr[i], arr[pivot_idx]
      pivot_idx += 1
  # eventually, swap arr[i] with arr[r] to have the condition that all the elements on the left side of i will be smaller than arr[i]
  # and all the elements on the right side of i will be greater than or equal to arr[i]
  arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]

  return pivot_idx

def find_k_smallest_element(nums:List[int], k:int) -> int:
  if k < 0 or k > len(nums):
    raise ValueError(f"{k} is our of range")

  left, right = 0, len(nums) - 1

  while left <= right:
    pivot_idx:int = partition(nums, left, right)
    if pivot_idx == k-1:
      return nums[pivot_idx]
    elif pivot_idx < k-1:
      left = pivot_idx + 1
    else: # pivot_idx > k
      right = pivot_idx - 1

  return -1

def find_k_largest_element(nums:List[int], k:int) -> int:
  if k < 0 or k > len(nums):
    raise ValueError(f"{k} is our of range")

  left, right = 0, len(nums) - 1

  while left <= right:
    pivot_idx:int = partition(nums, left, right)
    if pivot_idx == len(nums) - k:
      return nums[pivot_idx]
    elif pivot_idx < len(nums) - k:
      left = pivot_idx + 1
    else: # pivot_idx > k
      right = pivot_idx - 1

  return -1

nums:List[int] = [2, 3, 9, 5, 4]
ans:int = find_k_largest_element(nums, 5)
print(f'ans = {ans}')