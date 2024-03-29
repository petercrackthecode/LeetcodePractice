# https://www.interviewcake.com/article/python3/logarithms?course=fc1&section=algorithmic-thinking
from typing import List


def merge_sort(list_to_sort: List[int]) -> List[int]:
    # Base case: lists with fewer than 2 elements are sorted
    if len(list_to_sort) < 2:
        return list_to_sort

    # Step 1: divide the list in half
    # We use integer division, so we'll never get a "half index"
    mid_index = len(list_to_sort) // 2
    left = list_to_sort[:mid_index]
    right = list_to_sort[mid_index:]

    # Step 2: sort each half
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Step 3: merge the sorted halves
    sorted_list = []
    current_index_left = 0
    current_index_right = 0

    # sorted_left's first element comes next
    # if it's less than sorted_right's first element or if sorted_right is exhausted
    while len(sorted_list) < len(left) + len(right):
        if ((current_index_left < len(left)) and
                (current_index_right == len(right) or sorted_left[current_index_left] < sorted_right[current_index_right])):
            sorted_list.append(sorted_left[current_index_left])
            current_index_left += 1
        else:
            sorted_list.append(sorted_right[current_index_right])
            current_index_right += 1

    return sorted_list


print(merge_sort([1, 1, 1, 1]))
