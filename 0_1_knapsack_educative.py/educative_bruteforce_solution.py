from typing import List

"""
*** ALGORITHM:
- Base case: If there are no items left to add or the maximum capacity of the knapsack has been reached, we return 0.
- Recursive case 1: If the current item has a weight less than or equal to the remaining capacity of the knapsack, it can be
added to the knapsack. At this point, we make two recursive calls to solve two sub-problems:
  - Find the maximum value of items we can include in the knapsack, while including the current item.
  - Find the maximum value of items we can include in the knapsack, while excluding the current item.
Of the two options, we choose the one that yields the higher value.
- Recursive case 2: On the other hand, if the weight of the item is greater than the remaining capacity of the knapsack, the item
cannot be added to the knapsack. Therefore, we use a recursive call to move on to the next item, without adding this item to the knapsack.

"""


def find_max_knapsack_profit_helper(
    capacity: int, weights: List[int], values: List[int], n: int
) -> int:
    """
    n represents the number of available items.

    - base case: if capacity is 0 or n (the number of available items) is 0, return 0
    - otherwise, if weights[n-1] > capacity, we cannot put the current item to the bag, return find_max_knapsack_profit_helper(capacity, weights, values, n-1)
    (we use n-1 because we start counting list's indices from 0)
    - otherwise, we can fit weights[n-1] to our bag, we have to decide to choose it or not since we want the max total value
    => return max(find_max_knapsack_profit_helper(capacity, weights, values, n-1), find_max_knapsack_profit_helper(capacity-weights[n-1], weights, values, n-1) + values[n-1])
    """
    if capacity == 0 or n == 0:
        return 0
    elif weights[n - 1] > capacity:
        return find_max_knapsack_profit_helper(capacity, weights, values, n - 1)
    else:
        return max(
            find_max_knapsack_profit_helper(capacity, weights, values, n - 1),
            find_max_knapsack_profit_helper(
                capacity - weights[n - 1], weights, values, n - 1
            )
            + values[n - 1],
        )


def find_max_knapsack_profit(
    capacity: int, weights: List[int], values: List[int]
) -> int:
    return find_max_knapsack_profit_helper(capacity, weights, values, len(weights))
