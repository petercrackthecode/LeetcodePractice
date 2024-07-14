class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        - the initial array is sorted (with distinct values)

         0  1  2  3  4  5  6
        [0, 1, 2, 4, 5, 6, 7] -> [0, 1, 2] + [4, 5, 6, 7]
        [4, 5, 6, 7, 0, 1, 2] | n = 7
        k = 3
        target = 0
        ans = 4

        rotation:
        - divide the array to 2 parts: nums[0:k] + nums[k:n]
        - put nums[k:n] at the front to form the new array: nums[k:n] + nums[0:k]

        - since the initial array is sorted, we can apply binary search
        - the rotated array is semi-sorted: nums[k:n] and nums[0:k] are sorted
        - if we find the point where the sort status is broken, we can apply binary search on 2 halves to find target.
         
         0  1  2  3  4  5  6
        [4, 5, 6, 7, 0, 1, 2]
                     l
                           r
                        m
        pivot_idx = 4
        
        m-1
            m
                m+1
        7 > 0

        # check for boundary
        pivot_idx is at the index of the start of the second subarray
        '''
        def get_pivot_idx() -> int:
            nonlocal nums
            left, right = 0, len(nums) - 1

            while left <= right:
                mid:int = (right - left) // 2 + left
                # condition when we've found the pivot
                if mid - 1 >= 0 and nums[mid] < nums[mid-1]:
                    return mid
                # condition when we'll move right (left = mid + 1)
                elif nums[mid] >= nums[0]:
                    # nums[mid] == nums[0] case: mid == 0 since nums only contains distinct values
                    left = mid + 1
                # condition when we'll move left (right = mid - 1)
                else:
                    right = mid - 1
            # no pivot index found => our array is fully sorted, which is equivalent to an entire array rotated
            return 0

        def scope_binary_search(left:int, right:int) -> int:
            nonlocal nums, target
            while left <= right:
                mid:int = (right-left)//2 + left
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target: # move right
                    left = mid + 1
                else: # move left
                    right = mid - 1

            return -1

        pivot_idx:int = get_pivot_idx() # 0 -> n - k - 1 (inclusively) in the current array

        search_left_half:int = scope_binary_search(0, pivot_idx - 1)
        #           search left half                              search right half
        return search_left_half if search_left_half != -1 else scope_binary_search(pivot_idx, len(nums) - 1)