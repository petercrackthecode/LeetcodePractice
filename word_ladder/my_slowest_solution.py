from collections import defaultdict, deque
from typing import DefaultDict, Set

def is_transformable(w1: str, w2: str) -> bool:
    if len(w1) != len(w2):
        return False
    had_diff = False
    for i, ch in enumerate(w1):
        w2_char = w2[i]
        if ch != w2_char:
            if had_diff:
                return False
            had_diff = True
    
    return True


def form_graph(graph: DefaultDict[str, Set[str]], wordList: List[str]) -> None:
    for i in range(len(wordList)):
        w1 = wordList[i]
        for j in range(i+1, len(wordList)):
            w2 = wordList[j]
            if is_transformable(w1, w2):
                graph[w1].add(w2)
                graph[w2].add(w1)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        form a graph of words where each key is a word (str) and the value are the words that you can transform to by changing one letter of that word (Set[str])
        Bfs thru the graph, starting from hit.
        have a queue nodes_by_level to operate the bfs.
        have a set called visited (Set[str]) to maintain the list of nodes we already unpacked.
        we'll have a tuple of (word: str, level: int) where level is to keep track of the ladder length so far.
        by the time we've reached a node (word, level), add the word to visited. 
        If the word equals to endWord, return level immediately.
        Then, unpack all the neighbors of that word from the graph. If a neighbor didn't exist in visited, add the neighbor to nodes_by_level with the level + 1: nodes_by_level.append((neighbor, level + 1))

        Return 0 (we haven't found any valid path.)
        """
        ans = len(wordList) + 1
        graph = defaultdict(set)
        form_graph(graph, wordList + [beginWord])
        # print('graph = ', graph)
        nodes_by_level = deque()
        visited = set()
        nodes_by_level.append((beginWord, 1))

        while bool(nodes_by_level):
            (word, level) = nodes_by_level.popleft()
            if word == endWord:
                return level
            visited.add(word)
            neighbors = graph[word]
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                nodes_by_level.append((neighbor, level + 1))

        return 0

"""
{
 'hot': {'hit', 'dot', 'lot'}, 
 'dot': {'hot', 'dog', 'lot'}, 
 'lot': {'hot', 'dot', 'log'}, 
 'hit': {'hot'}, 
 'dog': {'dot', 'log', 'cog'}, 
 'log': {'dog', 'lot', 'cog'}, 
 'cog': {'dog', 'log'}
}
"""

