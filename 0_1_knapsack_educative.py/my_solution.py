from typing import List


def find_max_knapsack_profit(capacity:int, weights: List[int], values: List[int]) -> int:
  cols:int = capacity + 1
  rows:int = len(weights) + 1
  val_by_weight:List[List[int]] = [[0 for _ in range(cols)] for __ in range(rows)]

  for item in range(1, rows):
    for avail_weight in range(1, cols):
      curr_weight = weights[item-1]
      if curr_weight > avail_weight:
        # pick the last one
        val_by_weight[item][avail_weight] = val_by_weight[item-1][avail_weight]
      else: # curr_weight >= avail_weight -> can fit the item in the bag
        curr_val = values[item-1]
        val_by_weight[item][avail_weight] = max(val_by_weight[item-1][avail_weight],\
          val_by_weight[item-1][avail_weight-curr_weight] + curr_val)

  return val_by_weight[rows-1][cols-1]