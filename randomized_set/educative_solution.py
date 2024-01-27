# https://leetcode.com/problems/insert-delete-getrandom-o1/
from random import randint


class RandomizedSet:
    """
    - We store our data in an array and use a hash map to track the location at which each data element 
    is stored in the array.
    - We use the hash map to look up the location of the element to delete.
    - Swap the last element in the array with the one to be deleted.
    - In the hash map, update the location of the element we just moved.
    - Delete the key-value pair of the target data element from the hash map and then delete the target element
    from our array.
    """

    def __init__(self):
        self.nums = []
        self.num_to_index = dict()
        self.size = 0

    def insert(self, val: int) -> bool:
        """
        - if val exists in self.num_to_index => return False
        - otherwise (val doesn't exist in self.num_to_index):
          - self.nums[self.size] = val
          - self.num_to_index[val] = self.size
          - increment self.size by 1.
        - return True
        """
        if val in self.num_to_index:
            return False
        # val doesn't exist in self.num_to_index => insert new elements
        if self.size >= len(self.nums):
            self.nums.append(val)
        else:
            self.nums[self.size] = val
        self.num_to_index[val] = self.size
        self.size += 1

        return True

    def remove(self, val: int) -> bool:
        """
        - if val doesn't exist in self.num_to_index: return False
        - otherwise (val exists in self.num_to_index => must remove):
          - get the index of element equals to val in nums: index = self.num_to_index[val]
          - swap self.nums[index] with the last element: self.nums[self.size-1]
          - assign self.num_to_index[self.nums[index]] = index
          - pop: self.num_to_index.pop(val)
          - decrement self.size by 1

        - return True

        r: RandomizedSet
        i: insert
        r: remove
        g: getRandom

        r  | i | i | r | i | r | g
        [] | 0 | 1 | 0 | 2 | 1 | []
        """
        if val not in self.num_to_index:
            return False
        index = self.num_to_index[val]
        self.nums[index], self.nums[self.size -
                                    1] = self.nums[self.size-1], self.nums[index]

        self.num_to_index[self.nums[index]] = index
        self.num_to_index.pop(val)

        self.size -= 1

        return True

    def getRandom(self) -> int:
        random_index = randint(0, self.size-1)
        return self.nums[random_index]
