from typing import List


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
