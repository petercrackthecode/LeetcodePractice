# https://leetcode.com/problems/insert-delete-getrandom-o1/
from random import choice


class RandomSet():
    def __init__(self):
        self.indexor = {}  # Maps the actual value to its index
        self.store = []   # Store the actual values in an array

    # Function to insert a value
    def insert(self, val):
        """
        Inserts a value in the data structure.
        Returns True if it did not already contain the specified element.
        """
        if val in self.indexor:
            return False
        # Insert the actual value as a key and its index as a value
        self.indexor[val] = len(self.store)
        # Append a new value to array
        self.store.append(val)
        return True

    # Function to remove a value
    def delete(self, val):
        """
        Removes a value from the data structure.
        Returns True if it contains the specified element.
        """
        if val in self.indexor:
            # swap the last element in the array with the element
            # to delete, update the location of the moved element
            # in its entry in the hash map
            last, i = self.store[-1], self.indexor[val]
            self.store[i], self.indexor[last] = last, i
            # delete the last element
            del self.indexor[val]
            self.store.pop()
            return True
        return False

    # Function to generate a random value
    def get_random(self):
        """
        Choose an element at random from the data structure.
        """
        return choice(self.store)
