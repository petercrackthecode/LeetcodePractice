import copy
from typing import List


def find_max_knapsack_profit(
    capacity: int, weights: List[int], values: List[int]
) -> int:
    items_count: int = len(weights)

    prev_row: List[int] = [0 for _ in range(capacity + 1)]
    curr_row: List[int] = [0 for _ in range(capacity + 1)]

    for row in range(items_count + 1):
        for col in range(capacity + 1):
            if row == 0 or col == 0:
                curr_row[col] = 0
            else:
                curr_weight: int = weights[row - 1]
                if curr_weight > col:
                    curr_row[col] = prev_row[col]
                else:  # curr_weight <= capacity
                    curr_row[col] = max(
                        prev_row[col], prev_row[col - curr_weight] + values[row - 1]
                    )

        prev_row = copy.deepcopy(curr_row)

    return prev_row[capacity]
