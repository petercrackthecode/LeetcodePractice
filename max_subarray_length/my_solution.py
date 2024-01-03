# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """
                          0  1 2  3 4
        nums =           [1,-1,5,-2,3], k = 3
        output = 4
                          0  1 2  3 4
        sum_till_index = [1, 0,5, 3,6]

        i = 3
        start = [0, 1, 2, 3]

        sum[0->3] = sum_till_index[3] - sum_till_index[-1]
        sum[1->3] = sum_till_index[3] - sum_till_index[0]
        sum[2 -> 3] = sum_till_index[3] - sum_till_index[1]
        sum[3->3] = sum_till_index[3] - sum_till_index[2]


        is there any subarray among the four above (sum[0->3], sum[1->3], sum[2->3], sum[3->3]) that is equal to k?
                                                    k
        sum_till_index[-1] = sum_till_index[3] - sum[0->3] = remainder

        have another dictionary to lookup the minimum index by the sum: lookup_min_index_by_sum (key: prefix sum: int, value: minimum index: int)

        for every index i from 0 -> len(nums) - 1 (inclusively), we have to see if we can get a subarray that sums to k and ends at i (the last element of that subarrray should be exactly nums[i])
        sum_till_index: each element at index i is a sum of subarray from 0 -> i
        how do we know among the start, there is an index start_i that subarray within the range [start_i, i] (inclusively) has the sum to k
        subarray = [1, -1, 5, -2]
        [5, -2]
        [3]

        prefix sum

        ans = 0
        have a dictionary called sum_till_index = {}. Assign sum_till_index[-1] = 0
        have another dictionary called lookup_min_index_by_sum (key: prefix sum: int, value: minimum index: int) to find the minimum index whose prefix sum is equal to a given key (defaultdict). initialize lookup_min_index_by_sum[0] = -1
        have a variable called sum_so_far to memoize the sum_so_far. sum_so_far = 0
        iterate i from 0 -> len(nums) - 1:
            assign sum_so_far to sum_so_far plus nums[i]
            assign: sum_till_index[i] is equal to sum_so_far
            get the remainder: equal to sum_till_index[i] - k
            if remainder exists in lookup_min_index_by_sum:
                index is equal to lookup_min_index_by_sum[remainder]
                if index is smaller than or equal to i:
                    assign: ans is equal to the max between ans and i - index

        return ans

        Time: O(N)
        Space: O(N)
        """
        ans = 0
        lookup_min_index_by_sum = defaultdict(int)
        lookup_min_index_by_sum[0] = -1
        sum_so_far = 0

        for i in range(len(nums)):
            sum_so_far += nums[i]
            if sum_so_far not in lookup_min_index_by_sum:
                lookup_min_index_by_sum[sum_so_far] = i

            remainder = sum_so_far - k
            if remainder in lookup_min_index_by_sum:
                start = lookup_min_index_by_sum[remainder]
                subarr_length = i - start
                ans = max(ans, subarr_length)

        return ans
