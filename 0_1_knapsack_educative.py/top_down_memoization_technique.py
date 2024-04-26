'''
we observe that two variables change in each recursive call:
- capacity: the capacity of the knapsack.
- n: the number of items to consider.

We will use a 2D table with the above two indexes to uniquely identify a subproblem and store its
solution. At any later time, when we encounter the same subproblem, we can fetch the stored result
from the table with a O(1) lookup instead of recalculating that subproblem.
'''
def find_max_knapsack_profit_helper(capacity, weights, values, n, dp):
  # Base case
  if n == 0 or capacity == 0:
    return 0
  
  # If we have already solved this problem, fetch the result from memory
  if dp[n][capacity] != -1:
    return dp[n][capacity]
  
  # Otherwise, we solve it and save the result in our lookup table
  if weights[n-1] <= capacity:
    dp[n][capacity] = max(values[n-1] + find_max_knapsack_profit_helper(capacity-weights[n-1], weights, values, n-1, dp),
                          find_max_knapsack_profit_helper(capacity, weights, values, n-1, dp))
    
  return dp[n][capacity]

def find_max_knapsack_profit(capacity, weights, values):
  n = len(weights)
  # Set up the dp table to store solutions to subproblems
  dp = [[-1 for i in range(capacity+1)] for j in range(n+1)]
  return find_max_knapsack_profit_helper(capacity, weights, values, n, dp)