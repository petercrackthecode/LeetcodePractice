# https://leetcode.com/problems/divisor-game/
from typing import List


class Solution:
    def divisorGame(self, n: int) -> bool:
        """
        n number on the chalkboard
        * Choosing any x with 0 < x < n and n % x == 0.
        * Replacing the number n on the chalkboard with n - x.

        Alice plays first
        return True if Alice wins the game, otherwise return False.


        Say n = 2 is True (proven)
        n = 3 is False if Alice plays first
        Each turn, can I pick a number x where 0 < x < n and (n - x) = 3

        Alice and Bob both want to choose a move that is flavorable for them to win.

        n =              2    | 3    | 4        | 5       | 6
        x =              1    | 1    | 1, 2     | 1       | 1, 2, 3 
        Alice result     win  | lose | win (1)  | lose(1) | win (1)

        n =              7    | 8       | 9        | 10       | 6
        x =              1    | 1, 2, 4 | 1, 3     | 1, 2, 5  | 1, 2, 3 
        Alice result     lose | win     | lose     | win | win (1)

        - have an array to save the result of previous moves from 1 to n: win_stat = [False]
        - iterate num from 2 to n (inclusively):
            - find the denom of num using a helper function denoms = get_denoms(num: int) -> List[int]
            - iterate thru all the denoms. for each denom:
                - see if win_stat[num - denom] is False. If so:
                    - win_stat[num] = True
                    - break the loop
                - otherwise, win_stat[num] = False
        """
        def get_denoms(num: int) -> List[int]:
            ans = []
            for i in range(1, num//2 + 1):
                if num % i == 0:
                    ans.append(i)

            return ans

        win_stat = [False, False]
        for num in range(2, n+1):
            denoms = get_denoms(num)
            can_win = False
            for denom in denoms:
                if not win_stat[num - denom]:
                    win_stat.append(True)
                    can_win = True
                    break
            if not can_win:
                win_stat.append(False)

        # print('win_stat = ', win_stat)

        return win_stat[n]
