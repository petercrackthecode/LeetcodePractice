# https://leetcode.com/problems/random-pick-with-weight/
from typing import List, Tuple
import random


class Solution:
    # Brute force solution
    def __init__(self, w: List[int]):
        #  0  1  2  3
        # [1, 3, 5, 3]
        #                   (num, idx_in_w)
        """
        ** Bruteforce approach:
        - Expand the list [1, 2, 4] -> [1, 2, 2, 4, 4, 4, 4], since the probablity of picking a number val is val/sum(w), and the expanded list has the len of sum(w), we just duplicate every number val by [val] times (i.e. 2 will show up twice).
        - Then, when we randomize the numbers from the entire list, 2 will have exactly 2/7 chance of being picked.
        - Since we need to return the index in w instead of the element, we have to save the tuple of (val, index_in_w) instead => our list will be as such [(1, 0), (2, 1), (2, 1), (4, 2), (4, 2), (4, 2), (4, 2)]
        - finally, randomize an index within the range [0, len(expanded) - 1], then return self.expanded[random_idx][1] (since we wanna return the index)
        """
        self.expanded: List[Tuple[int, int]] = []

        for i, num in enumerate(w):
            for _ in range(num):
                self.expanded.append((num, i))

    def pickIndex(self) -> int:
        random_num: int = random.randint(0, len(self.expanded) - 1)
        return self.expanded[random_num][1]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
