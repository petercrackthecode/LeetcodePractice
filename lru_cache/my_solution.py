# https://leetcode.com/problems/lru-cache/

from typing import Optional
from collections import defaultdict


class Node:
    def __init__(self, key: int = -1, val: int = -1, prev: Optional["Node"] = None, next: Optional["Node"] = None):
        self.key: int = key
        self.val: int = val
        self.prev: Optional["Node"] = prev
        self.next: Optional["Node"] = next

    def set_next(self, next: Optional["Node"]) -> None:
        self.next = next

    def get_next(self) -> Optional["Node"]:
        return self.next

    def set_prev(self, prev: Optional["Node"]) -> None:
        self.prev = prev

    def get_prev(self) -> Optional["Node"]:
        return self.prev

    def get_val(self) -> int:
        return self.val

    def get_key(self) -> int:
        return self.key


class LRUCache:
    def __init__(self, capacity: int):
        """
        - head is the most recently used node
        - tail is the least recently used node.
        """
        self.capacity = capacity
        self.curr_size = 0
        self.node_lookup = dict()
        self.head: Optional["Node"] = None
        self.tail: Optional["Node"] = None

    def move_to_head(self, node: Optional["Node"]) -> None:
        if not node or not self.node_lookup[node.key] or node == self.head:
            return
        # node is different from self.head and node is in the list => node.prev is not empty
        # self.node_lookup[node.key] exists => our linked list is not empty => self.head & self.tail is not empty
        if node.prev:
            node.prev.next = node.next
        if node == self.tail:
            # node is the last node in the list
            if self.tail:
                self.tail = self.tail.prev
        else:
            # node is not the last node in the list => node.next is not empty
            if node.next:
                node.next.prev = node.prev
        # move the node to the beginning
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node

    def add_to_head(self, new_node: Optional["Node"]) -> None:
        if not new_node or new_node.key == -1 or new_node.val == -1:
            return
        key, val = new_node.key, new_node.val
        if not self.head or not self.tail:
            self.head = self.tail = new_node
        else:  # self.head is not empty
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.curr_size += 1
        self.node_lookup[key] = new_node

    def remove_last(self) -> None:
        key = -1

        if self.curr_size == 0:
            return
        elif self.curr_size == 1 and self.head and self.tail:
            key = self.head.key
            self.head = self.tail = None
        else:  # self.curr_size > 1 => we have at least 2 nodes in the list
            if self.tail and self.tail.prev:
                key = self.tail.key
                self.tail.prev.next = None
                self.tail = self.tail.prev

        self.curr_size -= 1
        self.node_lookup.pop(key)

    def get(self, key: int) -> int:
        if key not in self.node_lookup:
            return -1
        found_node = self.node_lookup[key]
        # if the found node is already the most recently used node (self.head), we don't need to move it. Otherwise, migrate it to the top
        self.move_to_head(found_node)

        return found_node.val

    def put(self, key: int, value: int) -> None:
        '''
        if the key already exists in the cache:
          - update the value of key.
          - update the prev and the next pointer of self.node_lookup[key]
          - migrate the self.node_lookup[key] node to the beginning of the linked list & update head.
        '''
        if key in self.node_lookup:
            node = self.node_lookup[key]
            node.val = value
            self.move_to_head(node)
        else:  # new node added in the list
            new_node = Node(key, value)
            self.add_to_head(new_node)

            if self.curr_size > self.capacity:
                self.remove_last()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
