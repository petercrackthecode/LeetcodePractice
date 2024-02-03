# https://leetcode.com/problems/lfu-cache
from collections import OrderedDict, defaultdict
from typing import DefaultDict

'''
Logic breakdowns:
- get and put methods both increment the counter
- we need to keep track of frequencies of a key and the value associated with the key.
- in order to drop the key with least frequency, we gotta know the minimum frequency at all times.
- among all the minimum frequency elements, we need the least recently used item to drop.
'''


class LFUCache:
    def __init__(self, capacity: int):
        self.frequencies: DefaultDict[int, OrderedDict] = defaultdict(
            lambda: OrderedDict())
        self.values = defaultdict(int)
        self.capacity = capacity
        self.min_freq = float('inf')

    def get(self, key: int) -> int:
        f = self.values[key]

        if not f:
            del self.values[key]
            return -1

        self.frequencies[f+1][key] = self.frequencies[f][key]
        self.values[key] = f+1

        del self.frequencies[f][key]

        if self.min_freq == f and not len(self.frequencies[f]):
            self.min_freq = f+1

        return self.frequencies[f+1][key]

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return

        if len(self.values) == self.capacity:
            if not self.values[key]:
                k = self.frequencies[int(self.min_freq)].popitem(last=False)
                del self.values[k[0]]

        f = self.values[key]
        self.values[key] += 1

        if f != 0:
            self.frequencies[f+1][key] = value
            del self.frequencies[f][key]

            if self.min_freq == f and not len(self.frequencies[f]):
                self.min_freq = f+1
        else:
            self.frequencies[f+1][key] = value

        self.min_freq = min(self.values[key], self.min_freq)
