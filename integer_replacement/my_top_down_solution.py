# https://leetcode.com/problems/integer-replacement/

class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        7 -> 6 -> 3 -> 2 -> 1

        13 -> 14 -> 7 -> 8 -> 4 -> 2 -> 1
        13 -> 12 -> 6 -> 3 -> 2 -> 1

        dynamic programming:
        memoize the result of a min steps that take to convert a number to 1 using a dictionary called min_steps (key: number: int, value: min_steps to convert the number to 1: int)
        have a helper function called integer_replace_helper(num: int) -> int to calculate the minimum number of steps it take to convert a number to 1:
            If num exists in min_steps, then return min_steps[num]
            otherwise, if num is an even number, save min_steps[num] = 1 + integer_replace_helper[num // 2]
            otherwise, num is an odd number. save min_steps[num] = 1 + min(integer_replace_helper(num + 1), integer_replace_helper(num-1))
            return min_steps[num]

        within our main function, return integer_replace_helper(n)
        """
        min_steps = {1: 0}

        def integer_replacement_helper(num: int) -> int:
            if num in min_steps:
                return min_steps[num]
            if num % 2 == 0:
                min_steps[num] = 1 + integer_replacement_helper(num // 2)
            else:
                min_steps[num] = 1 + min(integer_replacement_helper(num + 1),
                                         integer_replacement_helper(num-1))

            return min_steps[num]

        return integer_replacement_helper(n)
