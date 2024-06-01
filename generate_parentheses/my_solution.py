# https://leetcode.com/problems/generate-parentheses/
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        n = 3
        - ((()))
        - (()())
        - (())()
        - ()(())
        - ()()()
        
        ** OBSERVATION
        - At each step, we can always push one open bracket to our queue as long as the total number of parentheses is less than n.
        - when we push one open bracket, we can increase our open_bracket_count by 1.
        - when our open bracket count is greater than 0, we can push in one close bracket.
        - when we push in one close bracket, we reduce our open_bracket_count by 1.
        - we should keep track of our total number of pairs of parentheses. we will have a variable called total_paren to keep track of that. We increment total_paren by 1 every time we increment our open_bracket_count by 1.
        - We should have a recursive function called generate_bracket(total_paren:int, open_bracket_count:int, pair_so_far:List[str]) -> None: to help us generate the bracket.

        ** ALGO:
        - ans:List[str] = []
        - generate_bracket(0, 0, [])
        - return ans
        '''
        ans:List[str] = []

        def generate_bracket(total_paren:int, open_bracket_count:int, pairs_so_far:List[str]) -> None:
            if total_paren == n and open_bracket_count == 0:
                ans.append(''.join(pairs_so_far))
                return

            # add an open bracket
            if total_paren < n:
                generate_bracket(total_paren+1, open_bracket_count+1, pairs_so_far + ["("])
            
            # add a close bracket
            if open_bracket_count > 0:
                generate_bracket(total_paren, open_bracket_count-1, pairs_so_far + [")"])

        generate_bracket(0, 0, [])
        
        return ans
