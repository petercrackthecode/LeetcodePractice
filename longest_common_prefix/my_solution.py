# https://leetcode.com/problems/longest-common-prefix/
def are_all_characters_at_the_position_even(strs: List[str], pos: int) -> bool:
    for i in range(len(strs)-1):
        if strs[i][pos] != strs[i+1][pos]:
            return False
    return True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str_length = float('+inf')
        for s in strs:
            shortest_str_length = min(shortest_str_length, len(s))
        # a list of characters
        ans = []
        for pos in range(shortest_str_length):
            if not are_all_characters_at_the_position_even(strs, pos):
                break

            ans.append(strs[0][pos])

        return ''.join(ans)
