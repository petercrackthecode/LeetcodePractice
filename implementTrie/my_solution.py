# https://leetcode.com/problems/implement-trie-prefix-tree/
from collections import defaultdict


class Trie:

    def __init__(self):
        self.start_char = defaultdict(Trie)

    def insert(self, word: str) -> None:
        characters = [char for char in word]
        temp = self.start_char
        for character in characters:
            if not character in temp:
                temp[character] = Trie()

            temp = temp[character].start_char
        # "None" is marked as the end of the string
        temp['None'] = Trie()

    def search(self, word: str) -> bool:
        characters = [char for char in word]
        temp = self.start_char
        for character in characters:
            if not character in temp:
                return False
            temp = temp[character].start_char

        return 'None' in temp

    def startsWith(self, prefix: str) -> bool:
        characters = [char for char in prefix]
        temp = self.start_char
        for character in characters:
            if not character in temp:
                return False
            temp = temp[character].start_char

        return True
