# https://leetcode.com/problems/lru-cache/

from typing import Optional


class Node:
    def __init__(self, key: int = -1, val: int = -1, before=None, after=None):
        self.key = key
        self.val = val
        self.before = before
        self.after = after


class LRUCache:
    def __init__(self, capacity: int):
        """
        - head is the most recently used node
        - tail is the least recently used node.
        """
        self.capacity = capacity
        self.curr_size = 0
        self.node_lookup = dict()
        self.head = None
        self.tail = None

    def print_list(self) -> None:
        temp = self.head
        print('printing in order of most recent -> least recent')
        while temp != None:
            print(f'({temp.key}, {temp.val})', end=' ')
            temp = temp.after
        print(f'\nself.node_lookup = {self.node_lookup}')
        print('________________________________')

    def get(self, key: int) -> int:
        # return -1 if the key doesn't exist in the cache
        # push the node to head as the most frequently used node.
        # print('within get')
        # print(f'key = {key}')
        # print('self.tail = ', self.tail)
        # if self.tail:
        #     print(f'self.tail.key = {self.tail.key}, self.tail.val = {self.tail.val}')
        # print('self.head = ', self.head)
        # if self.head:
        #     print(f'self.head.key = {self.head.key}, self.head.val = {self.head.val}')
        # print("______________________________________________________________________")
        print('list before get: ')
        self.print_list()
        if key not in self.node_lookup:
            return -1
        found_node = self.node_lookup[key]
        print(
            f'found_node.key = {found_node.key}, found_node.val = {found_node.val}')
        self.print_list()
        if self.curr_size > 1:
            if found_node == self.tail:
                self.tail = self.tail.before
            found_node.before.after = found_node.after
            if found_node.after != None:
                found_node.after.before = found_node.before
            self.head.before = found_node
            found_node.after = self.head
            self.head = found_node

        print('list after get: ')
        self.print_list()
        return found_node.val

    def print_node(self, node: Optional[Node]) -> None:
        if not node:
            print("None")
        else:
            print(f'node.key = {node.key}, node.val = {node.val}')

    def put(self, key: int, value: int) -> None:
        '''
        if the key already exists in the cache:
          - update the value of key.
          - update the prev and the next pointer of self.node_lookup[key]
          - migrate the self.node_lookup[key] node to the beginning of the linked list & update head.
        '''
        print('list before put: ')
        self.print_list()
        if key in self.node_lookup:
            node = self.node_lookup[key]
            node.val = value
            # if the node is already the most recently used (head), do nothing
            if node == self.head:
                return
            before = node.before
            after = node.after
            # before is not null because node is not head
            before.after = after
            # after can be null (node == tail)
            if after:
                after.before = before
            node.before = None
            node.after = self.head
            self.head.before = node
            self.head = node
        else:  # new node added in the list
            new_node = Node(key, value, None, self.head)
            if self.curr_size == 0:  # empty list
                self.head = self.tail = new_node
            else:
                self.head.before = new_node
                self.head = new_node
            self.node_lookup[key] = new_node
            self.curr_size += 1

            print('list after put: ')
            self.print_list()
            if self.curr_size > self.capacity:
                # we need to remove the least recently used node at tail
                # print('self.curr_size = ', self.curr_size, ', self.capacity = ', self.capacity)
                print('self.tail = ', end='')
                self.print_node(self.tail)
                print('>>>>>>>>>>>>>>>>>>>>>>>>>')
                deleted_key = self.tail.key
                self.tail.before.after = None
                self.tail = self.tail.before
                self.curr_size = self.capacity
                del self.node_lookup[deleted_key]
                print('list after unloading from cache: ')
                self.print_list()
