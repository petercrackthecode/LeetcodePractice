# https://leetcode.com/problems/shortest-word-distance-ii/
from typing import DefaultDict, List
from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        '''
        - we can have repeated strings in wordsDict.
        - have a dictionary called word_indices:DefaultDict[str, List[int]] = defaultdict(list) where given a word (key: str), return a list of index where wordsDict[index] equals that word
        - loop thru each word at index i in wordsDict:
            - append i to word_indices[word]
        - shortest function:
            - word_1_indices:List[int] = word_indices[word_1]
            - word_2_indices:List[int] = word_indices[word_2]
            - return the value of the helper function find_smallest_gap_between_sorted_lists(word_1_indices, word_2_indices) (find_smallest_gap_between_sorted_lists(l1:List[int], l2:List[int]) -> int)
        '''
        self.word_indices:DefaultDict[str, List[int]] = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.word_indices[word].append(i)

    def shortest(self, word_1: str, word_2: str) -> int:
        def find_smallest_gap_between_sorted_lists(l1: List[int], l2: List[int]) -> int:
            '''
            ans:int = 3 * 10**4 + 1
            
                  p1
            l1 = [1, 7, 9]
                  p2
            l2 = [3, 4, 10]

            loop: while p1 < len(l1) and p2 < len(p2):
                ans = min(ans, abs(l1[p1] - l2[p2]))

                if p1+1 is greater than or equal to len(l1)-1:
                    move p2: p2 += 1
                otherwise, if p2+1 is greater than or equal to len(l2)-1:
                    move p1: p1 += 1
                otherwise, if abs(l1[p1+1] - l2[p2]) > abs(l1[p1] - l2[p2+1]):
                    move p2: p2 += 1
                otherwise:
                    move p1: p1 += 1
            '''
            ans:int = 3 * 10**4 + 1
            p1 = p2 = 0

            while p1 < len(l1) and p2 < len(l2):
                ans = min(ans, abs(l1[p1] - l2[p2]))

                if p1+1 >= len(l1):
                    p2 += 1
                elif p2+1 >= len(l2):
                    p1 += 1
                # p1+1 < len(l1) and p2+1 < len(l2)
                elif abs(l1[p1+1] - l2[p2]) > abs(l1[p1] - l2[p2+1]):
                    p2 += 1
                else:
                    p1 += 1

            return ans

        word_1_indices:List[int] = self.word_indices[word_1]
        word_2_indices:List[int] = self.word_indices[word_2]

        return find_smallest_gap_between_sorted_lists(word_1_indices, word_2_indices)

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)