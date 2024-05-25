# https://leetcode.com/problems/subsets/
from typing import List, Set, Tuple

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        - we always have an empty list [] within our answer.
        - we cannot have duplicate subsets.
        - each subset of length n is made up of another subset of length (n-1) combined with a subset of length 1.
        - nums is made up of unique elements.
        
        *******
        nums = [1,2,3]
        length:
            - 0: []
            - 1: [1], [2], [3]
            - 2: [1, 2], [1, 3], [2, 3]
            - 3: [1, 2, 3]

        [1, 2, 3]

        - ans:List[Set[List[int]]] = [{} for _ in range(len(nums) + 2)]

        - to form a subset of length n:
            - loop thru each subset of length n-1:
                - loop thru each element e within the subset of length 1:
                    - if e is already in the subset{n-1}: skip it.
                    - otherwise:
                        - new member of the subset{n}:
                            - add e to subset{n-1}: elem{n} = subset{n-1} + {e}
                            - sort elem{n} ascendingly
                            - add elem{n} to ans{n} if elem{n} doesn't exist within ans{n}

        - flatten ans to be a list of lists of int: flattened_ans = flatten_list(ans)
        - return flattened_ans
        '''
        # size: 0 -> len(nums) -> n+1 elments
        ans:List[Set[Tuple[int]]] = [set() for _ in range(len(nums) + 1)]

        ans[0] = set(())
        ans[1] = set(tuple([num]) for num in nums)

        for size in range(2, len(nums)+1):
            prev_list:Set[Tuple[int]] = ans[size-1]
            lst_of_size_1:Set[Tuple[int]] = ans[1]

            #   Tuple[int]
            for subset in prev_list:
                #   Tuple[int]
                for size_1_tuple in lst_of_size_1:
                    elem:int = size_1_tuple[0]
                    # elem doesn't exist within the tuple of subset
                    if subset.count(elem) == 0:
                        new_subset:Tuple[int] = tuple(sorted(subset + size_1_tuple))
                        ans[size].add(new_subset)

        flattened_ans:List[List[int]] = []

        #   Set[Tuple[int]]
        for subset in ans:
            if not bool(subset):
                flattened_ans.append([])
            else: # subset is not empty
                for _tuple in subset:
                    flattened_ans.append(list(_tuple))

        return flattened_ans
