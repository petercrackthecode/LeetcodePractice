# https://leetcode.com/problems/daily-temperatures/description/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        ** REASONING **
        return a list of int: List[int]
        answer[i]: number of days you have to wait after the i-th day to get a warmer temperature
        day j is warmer than day i if temperatures[j] > temperatures[i]

        ** TESTS **
                        0  1  2  3  4  5  6  7
                                 i
                                          j
        temperatures = [73,74,75,71,69,72,76,73]
        answer       = [1, 1, 4, 2, 1, 1, 0, 0]

         b
         t
        [(76, 6), (73, 7)]

        ans = [1, 1, 4, 2, 1, 1, 0, 0]

        - have a list ans prepopulated with len(temperatures) number of zeroes: ans = [0 for _ in range(len(temperature))]
        - have a stack of tuples: non_increasing_temps:List[Tuple[int, int]] = []
        - iterate thru the temperatures array: for each temperature at index i:
            - while non_increasing_temps is not empty and temperature is greater than the top temperature in non_increasing_temps (non_increasing_temps[-1][0]):
                - pop the bottom of the stack (or the top of the queue): index = non_increasing_temps.pop()[1]
                - assign: answer[index] = i - index
                - push temperature to the stack: non_increasing_temps.append((temperature, i))

        answer[0]: answer[0] < answer[1] (73 < 74) => 1-0 = 1
        answer[1]: answer[1] < answer[2] (74 < 75) => 2-1 = 1

        ** APPROACH:
        + Bruteforce:
        - loop from index i = 0 to len(temperatures) - 1:
            - have a variable called warmer_day_gap:int = 0
            - loop from index j = i+1 to len(temperatures)-1:
                - if temperatures[j] > temperature[i]:
                    - assign: warmer_day_gap = j - i
                    - break the loop.
            - append warmer_day_gap to answer.

        + Time: O(N^2)
        + Space: O(1)

        temperatures = [73,74,75,71,69,72,76,73]
        answer       = [1, 1, 4, 2, 1, 1, 0, 0]

         b
         t
        [(76, 6), (73, 7)]

        ans = [1, 1, 4, 2, 1, 1, 0, 0]

        - have a list ans prepopulated with len(temperatures) number of zeroes: ans = [0 for _ in range(len(temperature))]
        - have a stack of tuples: non_increasing_temps:List[Tuple[int, int]] = []

        - iterate thru the temperatures array: for each temperature at index i:
            - while non_increasing_temps is not empty and temperature is greater than the top temperature in non_increasing_temps (non_increasing_temps[-1][0]):
                - pop the bottom of the stack (or the top of the queue): index = non_increasing_temps.pop()[1]
                - assign: answer[index] = i - index
            - push temperature to the stack: non_increasing_temps.append((temperature, i))
        """
        ans = [0 for _ in range(len(temperatures))]
        non_increasing_temps: List[Tuple[int, int]] = []

        for i, temp in enumerate(temperatures):
            while bool(non_increasing_temps) and temp > non_increasing_temps[-1][0]:
                index = non_increasing_temps.pop()[1]
                ans[index] = i - index
            non_increasing_temps.append((temp, i))

        return ans
