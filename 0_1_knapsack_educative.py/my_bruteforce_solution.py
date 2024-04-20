'''
You are given n items whose weights and values are known, as well as a knapsack to carry these items. The knapsack cannot carry more than a certain maximum weight, known as its capacity.

You need to maximize the total value of the items in your knapsack, while ensuring that the sum of the weights of the selected items does not exceed the capacity of the knapsack.

If there is no combination of weights whose sum is within the capacity constraint, return 0.

Notes:
1. An item may not be broken up to fit into the knapsackm i.e., an item either goes into the knapsack in its entirety
or not at all.
2, We may not add an item more than once to the knapsack.

Constraints:
- 1 <= capacity <= 10^4
- 1 <= values.length <= 10^3
- weights.length == values.length
- 1 <= values[i] <= 10^4
- 1 <= weights[i] <= capacity
'''

'''
TESTS 1
capacity = 6
            0  1  2  3
weights  = [1, 2, 3, 5]
values   = [1, 5, 4, 8]

1 + 5 => 1 + 8 = 9
1 + 2 + 3 (6) = 1 + 5 + 4 = 10

- pick an element among the weights
- reduce the remaining weights

                                      6
                            /(1)  /(2) |(3) \(5)
                           5     4     3     1
                      /(2) |(3) 
'''

from typing import List, Set


def find_max_knapsack_profit(capacity:int, weights: List[int], values: List[int]) -> int:
  '''
  - need a helper function to handle the recursion called: calc_possible_profits(remaining_cap: int, avail_indices: Set[int], total_value: int) -> None
  - need to keep track of which indices in weights/values we already used.
  - we gotta have a variable to keep track of the max_value got from knapsack. This is the value we're going to return
  in the end.
  - at each step of the recursive call, we have to update the values & compare it with the max_value to get the updated
  max_value.
  - within the loop, we should ignore the indices whose weight is greater than our remaining capacity.
  '''
  max_value:float = float('-inf')

  def calc_possible_profits(remaining_cap: int, avail_indices: Set[int], total_value: int) -> None:
    nonlocal weights, values, max_value

    max_value = max(max_value, total_value)

    for i in avail_indices:
      weight:int = weights[i]
      if weight > remaining_cap:
        continue
      # weight <= remaining_cap
      new_cap:int = remaining_cap - weight
      new_total_value = total_value + values[i]
      calc_possible_profits(new_cap, avail_indices - {i}, new_total_value)


  calc_possible_profits(capacity, set(range(len(weights))), 0)

  return int(max_value)


