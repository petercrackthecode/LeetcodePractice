# https://leetcode.com/problems/lfu-cache
from collections import OrderedDict, defaultdict
from typing import DefaultDict

'''
Logic breakdowns:
- get and put methods both increment the counter
- we need to keep track of frequencies of a key and the value associated with the key.
- in order to drop the key with least frequency, we gotta know the minimum frequency at all times.
- among all the minimum frequency elements, we need the least recently used item to drop.

We keep two data structures, use_freq_lookup and group_dict_by_use_freq:
- use_freq_lookup: given a key, returns its use_frequency:
    - key: a key: int
    - value: the frequency of the said key: int
- group_dict_by_use_freq:
    - key: an use frequency: int
    - value: a dictionary of (key: int, value: int) whose frequencies == key: OrderedDict because we want to maintain
    an lru cache.
'''


class LFUCache:
    def __init__(self, capacity: int):
        # given a use frequency as a key, return a dictionary of keys and values that share
        # that same use frequency.
        self.group_dict_by_use_freq: DefaultDict[int, OrderedDict[int, int]] = defaultdict(
            lambda: OrderedDict())
        # given a key, return its use frequency
        self.use_freq_lookup = defaultdict(int)
        self.capacity = capacity
        self.min_freq = 4 * 10**5

    def get(self, key: int) -> int:
        if key not in self.use_freq_lookup:
            return -1

        freq = self.use_freq_lookup[key]
        new_freq = freq + 1
        # since we're getting the said key, its frequency is incremented by 1.
        # => move the said key to a new frequency.
        self.group_dict_by_use_freq[new_freq][key] = self.group_dict_by_use_freq[freq][key]
        # increment the use frequency of the said key
        self.use_freq_lookup[key] = new_freq

        # remove the key from the old frequency
        del self.group_dict_by_use_freq[freq][key]

        # if the key we've just incremented has the smallest frequency and it is the only one with that frequency
        # update the self.min_freq to the new frequency
        if len(self.group_dict_by_use_freq[self.min_freq]) == 0:
            self.min_freq = new_freq

        return self.group_dict_by_use_freq[new_freq][key]

    def put(self, key: int, value: int) -> None:
        # if the cache's capacity is 0 (Falsy value), we cannot add any element to it.
        if not self.capacity:
            return

        # our cache is full
        if len(self.use_freq_lookup) == self.capacity:
            # and we're adding in a new key => we must remove the key with the lfu and lru.
            if not self.use_freq_lookup[key]:
                # gotta convert self.min_freq to an int type since we initially set it to float('inf') as the
                # dummy value
                min_freq = int(self.min_freq)
                # pop the least recently used key among the keys with the lowest use frequencies
                lru_key, _ = self.group_dict_by_use_freq[min_freq].popitem(
                    last=False)
                del self.use_freq_lookup[lru_key]

        curr_freq = self.use_freq_lookup[key]
        new_freq = curr_freq + 1
        self.use_freq_lookup[key] = new_freq

        if curr_freq != 0:  # existing key
            self.group_dict_by_use_freq[new_freq][key] = value
            del self.group_dict_by_use_freq[curr_freq][key]

            if self.min_freq == curr_freq and not len(self.group_dict_by_use_freq[curr_freq]):
                self.min_freq = new_freq
        else:  # new key
            self.group_dict_by_use_freq[new_freq][key] = value

        # make sure our new_freq is always the smallest
        self.min_freq = min(self.use_freq_lookup[key], self.min_freq)
