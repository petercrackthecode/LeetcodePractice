# https://leetcode.com/problems/insert-delete-getrandom-o1/
from random import randint


class RandomizedSet:
    def __init__(self):
        self.index_to_num = dict()
        self.num_to_index = dict()
        self.nums = set()
        self.size = 0

    def insert(self, val: int) -> bool:
        """
        - insert an item val into the set if not present
        - return True if the item was not present
        - otherwise, return False
        """
        if val in self.nums:
            return False
        # insert a new element
        self.nums.add(val)
        self.index_to_num[self.size] = val
        self.num_to_index[val] = self.size
        self.size += 1

        return True

    def remove(self, val: int) -> bool:
        """
        - remove an item val from the set if present
        - return True if the item was present.
        - Otherwise, return False

        - whenever we remove an element val:
            - remove val from self.nums
            - swap the element with the last index in self.index_to_num
            - remove val from self.num_to_index (since val doesn't exist anymore => no index should be found)
            - update self.num_to_index[last_element] to val's previous index.
            - decrement self.size by 1
        - last element will be at the position self.size - 1
        """
        if val not in self.nums:
            return False
        # val in self.nums
        self.nums.discard(val)
        if val in self.num_to_index:
            index = self.num_to_index[val]
            last_element = self.index_to_num[self.size-1]
            # swap the current element with the last element, and update the 2 dictionaries accordingly
            self.index_to_num[index], self.index_to_num[self.size -
                                                        1] = last_element, val
            self.num_to_index.pop(val)
            self.num_to_index[last_element] = index
        self.size -= 1

        return True

    def getRandom(self) -> int:
        """
        we can do random number generator with the randint(from, to) function
        - convert the set to a list: nums_list - O(N) | N = len(nums)
        - use random_idx = randint(0, len(list) - 1)
        - return nums_list[random_idx]

        if we convert the set from the list, we get the list's indices, which we are used to retrieve an element after getting random_idx

        use a dictionary and a set:
        - dictionary: index_to_num: Dict[int, int]:
            - key: the indices from 0 to len(index_to_num) - 1
            - value: the numbers within the set nums
        - a set to save the numbers: nums: Set[int]
        - have another member variable called self.size = 0 to save the current number of elements within nums.
        index starts counting from 0
        """
        random_index = randint(0, self.size-1)
        return self.index_to_num[random_index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
