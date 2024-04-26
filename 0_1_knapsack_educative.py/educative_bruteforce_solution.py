from typing import List

def find_max_knapsack_profit_helper(capacity: int, weights: List[int], values: List[int], n: int):
  # Base case
  if n == 0 or capacity == 0:
    return 0
  
  # Recursive case
  # If the weight of the nth item is less than capacity, then:
  if weights[n-1] <= capacity:
    # We either include the item and deduct the weight of item from the knapsack capacity (to get the remaining capcity)
    # or, we don't include the item at all. We pick the option that yields the highest value.
    return max(
      values[n-1] + find_max_knapsack_profit_helper(capacity - weights[n-1], weights, values, n-1),
      find_max_knapsack_profit_helper(capacity, weights, values, n-1)
    )
  else:
    # Item can't be added to our knapsack if its weight is greater than the capacity
    return find_max_knapsack_profit_helper(capacity, weights, values, n-1)

def find_max_knapsack_profit(capacity, weights, values):
  n = len(weights)
  return find_max_knapsack_profit_helper(capacity, weights, values, n)