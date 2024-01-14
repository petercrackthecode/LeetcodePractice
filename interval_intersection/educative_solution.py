# https://leetcode.com/problems/interval-list-intersections/description/
from typing import List


def intervals_intersection(interval_list_a: List[List[int]], interval_list_b: List[List[int]]) -> List[List[int]]:
    intersections = []  # to store all intersecting intervals
    # index "i" to iterate over the length of list a and index "j"
    # to iterate over the length of list b
    i = j = 0

    # while loop will break whenever either of the lists ends
    while i < len(interval_list_a) and j < len(interval_list_b):
        # Let's check if interval_list_a[i] intersects interval_list_b[j]
        #  1. start - the potential startpoint of the intersection
        #  2. end - the potential endpoint of the intersection
        start = max(interval_list_a[i][0], interval_list_b[j][0])
        end = min(interval_list_a[i][1], interval_list_b[j][1])

        if start <= end:    # if this is an actual intersection
            intersections.append([start, end])   # add it to the list

        # Move forward in the list whose interval ends earlier
        if interval_list_a[i][1] < interval_list_b[j][1]:
            i += 1
        else:
            j += 1

    return intersections
