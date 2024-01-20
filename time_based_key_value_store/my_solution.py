# https://leetcode.com/problems/time-based-key-value-store/
"""
custom binary search

data structure:
- have a dictionary called self.timemap:
    - key: a key: str
    - value: a set of corresponding pair of (timestamp: int, value: str): Set[Tuple[int, str]]
"""
from collections import defaultdict
from typing import List, DefaultDict, Tuple


class TimeMap:

    def __init__(self):
        self.timemap: DefaultDict[str,
                                  List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        def custom_binary_search(values_thru_timestamps: List[Tuple[int, str]]) -> int:
            nonlocal timestamp

            if len(values_thru_timestamps) <= 0 or timestamp < values_thru_timestamps[0][0]:
                return -1

            left, right = 0, len(values_thru_timestamps) - 1
            while left <= right:
                mid = left + (right - left) // 2
                curr_timestamp = values_thru_timestamps[mid][0]
                # right boundary
                if mid == len(values_thru_timestamps) - 1 and curr_timestamp <= timestamp:
                    return mid
                elif curr_timestamp <= timestamp and values_thru_timestamps[mid+1][0] > timestamp:
                    return mid
                elif curr_timestamp > timestamp:
                    # move left
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        values_thru_timestamps = self.timemap[key]
        found_index = custom_binary_search(values_thru_timestamps)

        if found_index == -1:
            return ""
        return values_thru_timestamps[found_index][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
