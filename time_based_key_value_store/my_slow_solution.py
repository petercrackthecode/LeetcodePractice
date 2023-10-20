from collections import defaultdict
from typing import List, Tuple


class TimeMap:
    """
    Find all the timestamp_prev <= timestamp
    for all the timestamp of the same key, we have to store those timestamps in a sorted manner. 

    all these timestamps & values have the same key: 5
    [(timestamp_1, value_1), (timestamp_2, value_2), (searched_timestamp, random_val), (timestamp_3, value_3)]
    this list are sorted by timestamps in ascending order (because it's provided in the problem statement that "All the timestamps timestamp of set are strictly increasing.")

    - Have a dictionary called self.time_val_lookup_by_key where:
        - key: str: a key
        - value: List[Tuple[int, str]]: a list of tuples where each tuple has the form (timestamp, value)
    """

    def __init__(self):
        self.time_val_lookup_by_key = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        new_pair = (timestamp, value)

        self.time_val_lookup_by_key[key].append(new_pair)

    def custom_binary_search(self, time_and_val_with_key: List[Tuple[int, str]], checked_timestamp: int) -> str:
        """
                  4
        [1, 3, 3, 3, 8, 11, 24]
        """
        [left, right] = [0, len(time_and_val_with_key) - 1]

        while left <= right:
            mid = left + (right - left) // 2
            (timestamp, val) = time_and_val_with_key[mid]
            if timestamp == checked_timestamp:
                return val
            elif timestamp < checked_timestamp:
                if mid == right or time_and_val_with_key[mid+1][0] > checked_timestamp:
                    return val
                left = mid + 1
            else:  # timestamp < checked_timestamp
                right = mid - 1

        return ""

    def get(self, key: str, timestamp: int) -> str:
        """
        timestamp_prev <= timestamp
        if there are multiple values where its _timestamp <= timestamp, return the value with the highest _timestamp

        - fetch the list of pairs (timestamp, val) at the given key:
            time_and_val_with_key = self.time_val_lookup_by_key[key]

        - with the given timestamp, apply custom binary search to find the greatest index that we can put time_stamp in time_and_val_with_key. have a function called custom_binary_search(time_and_val_with_key: List[Tuple[int, str]], timestamp: int) to help us to do


        [(0, 3), (1, 2), (1, 4), [1, 7]]

        Question to ask: at a given timestamp, can we have 2 value? yes
        """
        time_and_val_with_key = self.time_val_lookup_by_key[key]
        if len(time_and_val_with_key) <= 0:
            return ""

        return self.custom_binary_search(time_and_val_with_key, timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
