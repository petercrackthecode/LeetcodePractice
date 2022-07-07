class Solution:
    def __init__(self):
        self.memoizedWays = {0: 1, 1: 1}

    def climbStairs(self, n: int) -> int:
        """
        Steps to solve the problem:
        1. In each step on the staircase, there are two options: you can either climb 1 or 2 steps.
           After having decided to climb one or two steps, you have a remaining number of steps left to climb.
           Pass that remaining number of steps to the climbStairs function as your new n.
           Base case: If n == 0, steps = += 1.
        2. Since we have repetitive steps for each n, we should memoize the steps to a dictionary for later reuse.
        """
        if n in self.memoizedWays:
            return self.memoizedWays[n]
        else:
            # There are at least 2 ways to climb the remaining steps:
            self.memoizedWays[n] = self.climbStairs(
                n-2) + self.climbStairs(n-1) if n >= 2 else self.climbStairs(n-1)

        return self.memoizedWays[n]
