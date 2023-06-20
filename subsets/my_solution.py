# https://leetcode.com/problems/subsets/
from typing import List, Deque, Set, Tuple
from collections import deque


def expand_one_level_lower_subsets(subset: List[int], subset_queue: Deque[List[int]], final_set: Set[Tuple[int]]) -> None:
    if len(subset) <= 1:
        return

    for index in range(len(subset)):
        smaller_subset = subset[:index] + subset[index+1:]
        subset_queue.append(smaller_subset)
        final_set.add(tuple(smaller_subset))


def get_2d_list_from_set_of_tuples(a_set: Set[Tuple[int]]) -> List[List[int]]:
    ans = [list(a_tuple) for a_tuple in a_set]
    return ans


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = {(), tuple(nums)}
        subset_queue = deque()
        subset_queue.append(nums)

        while len(subset_queue) > 0:
            subset = subset_queue.popleft()
            expand_one_level_lower_subsets(subset, subset_queue, ans)

        return get_2d_list_from_set_of_tuples(ans)

    """
    + num array's length is n. Starting from len(nums) == n. We have one single subset: the full list nums. Push
    that array into a queue. Call the queue subset_queue
    + Start ans as a set of tuples, then convert it to a 2d list once we return it.
    + Then, while len(subset_queue) > 0:
        subset = subset_queue.popleft()
        ans.append(subset)
        expand_one_level_lower_subsets(subset, subset_queue, ans) (expand_one_level_lower_subsets(subset, subset_queue, ans) -> None is a
        function that get all the one-level-lower subsets and push it to the subset_queue and ans)

    """
