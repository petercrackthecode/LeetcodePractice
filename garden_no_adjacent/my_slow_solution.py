# https://leetcode.com/problems/flower-planting-with-no-adjacent/description/
from typing import List, Dict, Set
from collections import defaultdict


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        """
        n gardens labeled from 1 to n
        paths[i] is an array of 2 elements.
        4 types of flowers
        at most 3 paths coming into or leaving the garden => a node has at most 3 edges
        choose flower type for each garden. For any two gardens connected by a path, have different type of flowers.
        
        paths = [
                    [1,2],
                    [2,3],
                    [3,1]
                ]
                
                1
               / \
              2 - 3
              
                1      3
               /        \
              2          4
              
              
             1------
            / \    |
           2 - 3 - 4
            \_____/
        
        graph coloring problem
        gotta get the available colors
        need recursion
        
        - have an array ans to return
        - have a dictionary called color_lookup:
            - key: node: int
            - value: the color of the said node: int
        - iterate thru every pairs in the paths array to form a graph called graph: Dict[int, Set[int]] (key: int- the node, value: Set[int]: neighbors to the node)
        - have a set called colored to save the node we already colored: colored = {}
        - pick each node in the graph:
            - if the node is already color (node in colored), skip it to the next node.
            - called the helper function color_node(node)
            
        - return ans
        """
        ans: List[int] = []
        color_lookup: Dict[int, int] = defaultdict(lambda: 1)
        graph: Dict[int, Set[int]] = defaultdict(set)
        colored: Set[int] = set()

        def color_node(node: int) -> None:
            nonlocal ans, color_lookup, graph, colored
            neighbors = graph[node]
            avail_colors: Set[int] = {1, 2, 3, 4}

            for neighbor in neighbors:
                if neighbor in colored:
                    neighbor_color = color_lookup[neighbor]
                    avail_colors -= {neighbor_color}

            if len(avail_colors) > 0:
                new_color = list(avail_colors)[0]
                colored.add(node)
                color_lookup[node] = new_color
                for neighbor in neighbors:
                    if not neighbor in colored:
                        color_node(neighbor)

        for [x, y] in paths:
            graph[x].add(y)
            graph[y].add(x)

        for node in graph.keys():
            if node in colored:
                continue
            color_node(node)

        for x in range(1, n + 1):
            ans.append(color_lookup[x])

        return ans
