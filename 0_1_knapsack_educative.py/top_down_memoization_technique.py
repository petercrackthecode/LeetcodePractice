from typing import List

"""
we observe that two variables change in each recursive call:
- capacity: the capacity of the knapsack.
- n: the number of items to consider.

We will use a 2D table with the above two indexes to uniquely identify a subproblem and store its
solution. At any later time, when we encounter the same subproblem, we can fetch the stored result
from the table with a O(1) lookup instead of recalculating that subproblem.
"""


def find_max_knapsack_profit_helper(
    capacity: int,
    weights: List[int],
    values: List[int],
    items_count: int,
    value_by_weight_and_cap: List[List[int]],
) -> int:
    # base case
    if (capacity == 0 or items_count == 0) or value_by_weight_and_cap[capacity][
        items_count
    ] != 0:
        return value_by_weight_and_cap[capacity][items_count]

    curr_weight: int = weights[items_count - 1]
    if curr_weight > capacity:
        value_by_weight_and_cap[capacity][items_count] = (
            find_max_knapsack_profit_helper(
                capacity, weights, values, items_count - 1, value_by_weight_and_cap
            )
        )
    else:  # curr_weight <= capacity
        value_by_weight_and_cap[capacity][items_count] = max(
            find_max_knapsack_profit_helper(
                capacity, weights, values, items_count - 1, value_by_weight_and_cap
            ),
            find_max_knapsack_profit_helper(
                capacity - curr_weight,
                weights,
                values,
                items_count - 1,
                value_by_weight_and_cap,
            )
            + values[items_count - 1],
        )

    return value_by_weight_and_cap[capacity][items_count]


def find_max_knapsack_profit(
    capacity: int, weights: List[int], values: List[int]
) -> int:
    # value_by_weight_and_cap[cap][item_count]
    value_by_weight_and_cap: List[List[int]] = [
        [0 for _ in range(len(weights) + 1)] for __ in range(capacity + 1)
    ]

    return find_max_knapsack_profit_helper(
        capacity, weights, values, len(weights), value_by_weight_and_cap
    )
