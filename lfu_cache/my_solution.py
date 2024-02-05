# https://leetcode.com/problems/lfu-cache
from typing import DefaultDict
from collections import defaultdict, OrderedDict

"""
    ["LFUCache","put","put","get","get","get","put","put","get","get","get","get"]
    [[3],[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]

out:[null,null,null,2,1,2,null,null,  3 ,2,-1,4]
exp:[null,null,null,2,1,2,null,null, -1 ,2,1,4]
"""


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.use_freq_lookup: DefaultDict[int, int] = defaultdict(int)
        self.group_key_by_use_freq: DefaultDict[int, OrderedDict[int, int]] = (
            DefaultDict(lambda: OrderedDict())
        )
        self.min_use_freq = 4 * 10**5

    """
    - If the key exists in the cache:
        - increment its use_count by 1.
        - move the key's to a new group of use_freq in self.group_key_by_use_freq
        - update self.min_use_freq if needed
        - return the value at key
    - otherwise, return -1
    """

    def get(self, key: int) -> int:
        if key not in self.use_freq_lookup:
            return -1

        # key in self.use_freq_lookup
        curr_use_freq = self.use_freq_lookup[key]
        next_use_freq = curr_use_freq + 1
        val = self.group_key_by_use_freq[curr_use_freq][key]

        self.use_freq_lookup[key] = next_use_freq
        self.group_key_by_use_freq[next_use_freq][key] = val
        self.group_key_by_use_freq[curr_use_freq].pop(key)

        # either we have no element with the (self.min_use_freq) frequency, or we have a new min_use_freq (self.min_use_freq > next_use_freq)
        if (
            len(self.group_key_by_use_freq[self.min_use_freq]) == 0
            or next_use_freq < self.min_use_freq
        ):
            self.min_use_freq = next_use_freq

        return val

    """    
    - if the key is already in the cache:
        - update its value in the cache.
    - if the key doesn't exist in the cache & the cache reaches its capacity (len(self.use_freq_lookup) == self.capacity):
        - get the lru_key from self.group_key_by_use_freq[self.min_use_freq]
        - remove the said lru_key from self.group_key_by_use_freq[self.min_use_freq]
        - remove the said lru_key from self.use_freq_lookup
    
    - curr_use_freq = self.use_freq_lookup[key]
    - next_use_freq = curr_use_freq plus 1
    - increment the use frequency of the key by 1, and update self.use_freq_lookup[key] accordingly.
    - remove key from self.group_key_by_use_freq[curr_use_freq] and add key & value to self.group_key_by_use_freq[next_use_freq]

    - if the self.group_key_by_use_freq[curr_use_freq] is empty:
        - update self.min_use_freq accordingly.
        - remove curr_use_freq from self.group_key_by_use_freq
    """

    def put(self, key: int, value: int):
        curr_use_freq = (
            0 if key not in self.use_freq_lookup else self.use_freq_lookup[key]
        )
        next_use_freq = curr_use_freq + 1

        # self.should_print and print(f'curr_use_freq = {curr_use_freq}')
        # self.should_print and print(f'len(self.use_freq_lookup) = {len(self.use_freq_lookup)}')

        # we've reached the capacity & a new key is being added.
        if curr_use_freq == 0 and len(self.use_freq_lookup) >= self.capacity:
            lru_key, _ = self.group_key_by_use_freq[self.min_use_freq].popitem(
                last=False
            )
            self.use_freq_lookup.pop(lru_key)

        self.use_freq_lookup[key] = next_use_freq
        if curr_use_freq in self.group_key_by_use_freq:
            self.group_key_by_use_freq[curr_use_freq].pop(key)
        self.group_key_by_use_freq[next_use_freq][key] = value

        # either we have no element with the (self.min_use_freq) frequency, or we have a new min_use_freq (self.min_use_freq > next_use_freq)
        if (
            len(self.group_key_by_use_freq[self.min_use_freq]) == 0
            or next_use_freq < self.min_use_freq
        ):
            self.min_use_freq = next_use_freq
