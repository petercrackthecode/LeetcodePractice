# https://leetcode.com/problems/letter-tile-possibilities/
from typing import Set, List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        backtracking?

        - we'll have sequences who lengths rank from 1 -> len(tiles)
        """
        ans: Set[str] = set()

        def form_sequence(sequence_left: int, used_index: Set[int], str_so_far: List[str]) -> None:
            if sequence_left <= 0:
                ans.add("".join(str_so_far))
                return

            for i in range(len(tiles)):
                if i in used_index:
                    continue
                new_used_index = used_index.union({i})
                new_str_so_far = str_so_far + [tiles[i]]

                form_sequence(sequence_left - 1, new_used_index, new_str_so_far)

        for sequence_left in range(1, len(tiles) + 1):
            form_sequence(sequence_left, set(), [])

        return len(ans)
