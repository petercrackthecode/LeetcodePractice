"""
- The function get and put must each run in O(1) average time complexity
Constraints:
- 1 <= capacity <= 10^4
- 0 <= key <= 10^5
- 0 <= value <= 10^9
- At most 2 * 10^5 calls will be made to get and put.
"""

"""
- use a use counter for each key in the cache. the key with the smallest use counter is the least frequently used key.
- should allow handling multiple keys with the same frequency.
- these multiple keys handling with the same frequency should support lru.
- should keep track of the current smallest use_counter.
- when a key is got or updated, we:
    - increment its use counter by 1: new_counter = old_counter + 1
    - within all the keys with the new_counter, the current key must be moved to the lru.
- when a key is inserted, its use_counter is set to 1.
"""
from typing import OrderedDict, DefaultDict
from collections import OrderedDict, defaultdict


class LFUCache:
    """
    - initialize the object with the capacity
    """

    def __init__(self, capacity: int):
        """
        - have a variable to lookup the use_count of a key: self.use_count (key: int, value: use_counter of the said key: int)
        - have a variable to keep track of the lowest use_frequency: self.min_use_count: int
        - have a variable to look up all the keys with the same use_count: self.group_keys_by_use_count: (key: use count: int, value: OrderedDict[int, int])
        - have capacity to remember the cache's maximum capacity
        """
        self.use_count: DefaultDict[int, int] = defaultdict(int)
        self.min_use_count: int = 0
        self.group_keys_by_use_count: DefaultDict[int, OrderedDict[int, int]] = defaultdict(
            OrderedDict
        )
        self.capacity = capacity

    """
    - If the key exists in the cache:
        - increment the use_counter of the key by 1.
        - update the self.min_use_count value if necessary
        - return the value at the key.
    - otherwise, return -1.
    """

    def get(self, key: int) -> int:
        if key not in self.use_count:
            return -1
        # the key exists in the cache
        old_use_count: int = self.use_count[key]
        new_use_count: int = old_use_count + 1
        val = self.group_keys_by_use_count[old_use_count][key]

        self.use_count[key] = new_use_count
        self.group_keys_by_use_count[old_use_count].pop(key)
        self.group_keys_by_use_count[new_use_count][key] = val

        # update our min_use_count
        if (
            new_use_count < self.min_use_count
            or len(self.group_keys_by_use_count[self.min_use_count]) <= 0
        ):
            self.min_use_count = new_use_count

        return val

    """
    - if the cache reaches its capacity and we are adding a new key:
        - remove the least frequently used key (the key with the lowest use_counter):
            - when there are multiple keys with the same smallest use_counter, return the least recently used (lru) key.
    """

    def put(self, key: int, value: int) -> None:
        # the cache reaches its capacity & we are adding a new key => remove the lfu key with the lru
        if len(self.use_count) == self.capacity and key not in self.use_count:
            lfu_keys: OrderedDict[int, int] = self.group_keys_by_use_count[self.min_use_count]
            removed_key, _ = self.group_keys_by_use_count[self.min_use_count].popitem(last=False)
            old_use_count: int = self.use_count[removed_key]
            # update self.use_count and self.min_use_count accordingly
            self.use_count.pop(removed_key)
            # old_use_count == self.min_use_count
            if len(lfu_keys) == 0:
                # adding a new key => self.min_use_count = 1 (minimum value for use_count)
                self.min_use_count = 1

        old_use_count = 0 if key not in self.use_count else self.use_count[key]
        new_use_count = old_use_count + 1
        self.use_count[key] = new_use_count
        if (
            old_use_count in self.group_keys_by_use_count
            and key in self.group_keys_by_use_count[old_use_count]
        ):
            self.group_keys_by_use_count[old_use_count].pop(key)
        self.group_keys_by_use_count[new_use_count][key] = value
        self.group_keys_by_use_count[new_use_count].move_to_end(key)
        if (
            new_use_count < self.min_use_count
            or len(self.group_keys_by_use_count[self.min_use_count]) <= 0
        ):
            self.min_use_count = new_use_count


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
