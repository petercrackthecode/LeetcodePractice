# https://leetcode.com/problems/lfu-cache/
from collections import defaultdict

# get and put must each run in O(1) average time complexity.
# when the key is first inserted into the cache, its use counter (or frequency) is set to 1
"""
Let's think about the case of removing the least frequently used key first (LRU-agnostic), then think of the edge case (tie of two or more keys with the same frequency) later.
"""


class LFUCache:
    """
    bruteforce:
    - implement the cache using a dictionary cache:
        - key: int
        - value: int
    - have another dictionary called use_counter = defaultdict(int):
        - key: int
        - value: the said key's use counter: int
    - put:
        - If the key already exists in cache:
            - update its new value in cache.
            - increment use_counter[key] by 1
        - otherwise:
            - if the cache reaches its capacity:
                - remove the least frequently used key:
                    - loop thru all the (key, counter) pair in use_counter, and find the key with the lowest counter (O(N)).
                    - If we have more than 1 key with the same use counter, remove the least recently used key => we gotta track for the orders.
            - cache[key] = value
            - use_counter[key] = 1

        We should have timestamp:int that increment each time an operation of get and put is used.
        And, another dictionary called last_used (key: int, value: the last timestamp the key is used: int) to look up the last time_stamp that a key is used:
    """
    # initialize the object with the capacity of the data structure

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.use_freq = defaultdict(int)
        self.cache = defaultdict(int)
        self.timestamp: int = 0
        self.last_used = defaultdict(int)
    # get the value of the key & return that value if the key exists in the cache.
    # Otherwise, return -1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.timestamp += 1
        self.last_used[key] = self.timestamp

        self.use_freq[key] += 1
        return self.cache[key]
    # - If the key exists in the cache, update its value
    # - Otherwise, insert the key with the value to the cache
    #
    # - When the cache reaches its max capacity, it should invalidates and removes the least frequently used key before inserting a new item.
    # - When there is a tie (two or more keys with the same frequency), the least recently used key (LRU) would be invalidated.

    def put(self, key: int, value: int) -> None:
        # we should have a map to keep track of the frequency of each key
        # bruteforce: have a dictionary called key_freq (key: int, value: use frequency of the said key: int) to keep track of the frequencies of each key.
        # when we do get or put, increment use_freq[key] by 1.
        # when we need to remove the least frequently used key, loop through the key_freq dictionary to find the key whose the frequency is the smallest, and remove that said key.

        # adding new key, but reached maximum capacity => need to remove the key with the lowest use frequency
        if key not in self.cache and len(self.cache) == self.capacity:
            keys_with_lowest_freq = [list(self.use_freq.keys())[0]]
            lowest_freq = self.use_freq[keys_with_lowest_freq[0]]

            for _key, freq in self.use_freq.items():
                if freq < lowest_freq:
                    keys_with_lowest_freq = [_key]
                    lowest_freq = freq
                elif freq == lowest_freq:
                    keys_with_lowest_freq.append(_key)

            removed_key = keys_with_lowest_freq[0]

            if len(keys_with_lowest_freq) > 1:
                # len(keys_with_lowest_freq) > 1 => more than one key with the lowest freq => find the key with the smallest self.last_used[key] (LRU)
                for _key in keys_with_lowest_freq:
                    if _key in self.last_used and self.last_used[_key] < self.last_used[removed_key]:
                        removed_key = _key
            self.cache.pop(removed_key)
            self.use_freq.pop(removed_key)
            self.last_used.pop(removed_key)

        self.cache[key] = value
        self.timestamp += 1
        self.last_used[key] = self.timestamp

        self.use_freq[key] += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
