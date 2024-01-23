# https://leetcode.com/problems/lru-cache/

class LRUCache:
    """
    get and put must each run in O(1) average space complexity

    [[2], [1, 1], [2, 2], [1], [3, 3], [1], [1], [3], [4]]
    we should also have a dictionary
    dict = {
        1: 1
        3: 3,
        4: 4
    }
    q1   = [[2, 2], [1, 1], [3, 3]]
    q2   = []

    should we check q1 first or q2 first?
    we should check q2 first because it contains the buffer of the most initial nodes

    decide when to push to the end and when to push to the beginning and when to push to the end of q2 and q1.

    size = 3
    the sum of 2 queue should be equal to the size.

    - 2 cases of put:
        - when the key already exists in the cache: the size of the cache won't change => no need to update the dictionary, but gotta update the queues
        - when the key doesn't yet exists in the cache.

    get & set must run in O(1) average time complexity
    """

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
