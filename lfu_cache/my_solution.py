# https://leetcode.com/problems/lfu-cache/
from typing import Optional, DefaultDict
from collections import OrderedDict, defaultdict

class UseFreqNode:
    def __init__(self, _use_freq: int = 1, _prev: Optional["UseFreqNode"] = None, _next: Optional["UseFreqNode"] = None):
        self.use_freq = _use_freq
        # the last key is the most recently used key
        # the first key is the least recently used key
        self.keys_with_use_freq = OrderedDict()
        self.prev = _prev
        self.next = _next

class LFUCache:
    """
    This problem's topics are Hash Table, Linked List, Design, and Doubly-Linked List.
    - Can we apply any methods we learned from the LRU cache problem?
    - Normally, we need to have a use_counter dictionary to keep track of the usage of a key. But, when we want to evade the least frequently used key (the key with the lowest use_counter point), we gotta loop through the entire use_counter dictionary to find it. Can we do better?
    - Also, there can be multiple keys with the same LFU count, so we gotta pick one key among them that least recently used. But, how do we know if a key is used before or after another key? If we bruteforce it, we traverse from head to tail and whenever we see a key exists in our LFU keys_list, we stop the traversal and remove that key.

    Should we have two dictionaries?
    Can we apply the dictionary with value linked to a doubly-linked list approach to the frequency?
    """

    # initializes the object with the capacity of the data structure
    def __init__(self, capacity: int):
        self.capacity = capacity
        # self.cache: key: key: int, value: value: int.
        self.cache: DefaultDict[int, int] = defaultdict(lambda: -1)
        self.use_freq_lookup: DefaultDict[int, Optional["UseFreqNode"]] = defaultdict(lambda: None)
        # These pointers represent the head & tail of the doubly linked list that point to the useFreq nodes.
        # self.use_freq_head is the smallest frequency
        self.use_freq_head: Optional["UseFreqNode"] = None
        # self.use_freq_tail is the greatest frequency
        self.use_freq_tail: Optional["UseFreqNode"] = None

    # given a key, increment the use frequency of that key by 1.
    def increment_use_freq(self, key: int) -> None:
        pass
    
    # if the key doesn't exist in the cache, return -1
    # otherwise, increment the key's use counter by 1 & return the value at key
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.increment_use_freq(key)

        return self.cache[key]
        
    # if the key already exists in the cache, update the value at the key.
    # Otherwise (the key doesn't exist in the cache => adding a new key):
    #   - if the cache reaches its capacity (len(self.cache) == self.capacity), remove the key with the smallest use_count. If there are multiple keys with the same smallest use_count, remove the lru key.
    #   - add the key with the value & increment the use_freq at that key.
    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.capacity:
            # remove the key with the smallest use_count and lru
            # the smallest frequency is at self.use_freq_head
            pass
        
        self.cache[key] = value
        self.increment_use_freq(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)