from heapq import *
from typing import List, Tuple
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        k = 2
        ans = ["i", "love"]
        - return the answer sorted by the frequency from highest to lowest: return a list of str: List[str]
        - sort the words with the same frequency by their lexicographical order:
            - ["a", "b"]
            - k = 1
            => "a"

        - count the frequency of the words, then rank the words from lowest to highest frequency.
        - to count the frequency, use a Counter called word_freq:Counter[str, int] = Counter(words)
        - Use a min_heap of pairs (freq:int, word:str): List[Tuple[int, str]]
        - loop: for each word, freq in word_freq.items():
            - if the length of min_heap is smaller than k:
                - push the pair (freq, word) to the min_heap
            - otherwise, if the current frequency (freq) is greater than or equal to the frequency at min_heap's root:
                - if freq is equal to the frequency of the word at min_heap's root:
                    - if the current word ranks before the word at min_heap:
                        - pop the root of min_heap
                        - push (freq)
        '''
        word_freq:Counter[str, int] = Counter(words)
        max_heap:List[Tuple[int, str]] = []
        ans:List[str] = []

        for word, freq in word_freq.items():
            heappush(max_heap, (-freq, word))

        for _ in range(k):
            _, word = heappop(max_heap)
            ans.append(word)

        return ans