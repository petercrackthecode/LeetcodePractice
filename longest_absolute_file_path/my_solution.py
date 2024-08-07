# https://leetcode.com/problems/longest-absolute-file-path/

import re
from typing import DefaultDict, List, Set, Dict
from collections import defaultdict


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """
        - longest absolute path to a file (not a directory)

        \n: exiting the current file/directory, reset the level to 0, go to a new file/directory
        \t: increment the level by 1.


        dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext

        dir
            subdir1
            subdir2
                file.ext

        nearest level 0: dir
        nearest level 1: subdir2
        nearest level 2: file.ext


        """
        new_str: str = re.sub("\n", "*", input)
        new_str: str = re.sub("\t", "#", new_str)

        graph: DefaultDict[str, Set] = defaultdict(set)
        curr_level: int = 0
        last_node_at_level: Dict[int, str] = dict()
        curr_str: List[str] = []
        level_0_node = set()
        ans: int = 0

        def dfs(curr_node: str, path_length: int):
            nonlocal graph, ans

            if "." in curr_node:  # a file
                ans = max(ans, path_length)

            for node in graph[curr_node]:
                new_length: int = path_length + 1 + len(node)
                dfs(node, new_length)

        for ch in new_str:
            if ch == "#":  # \t
                curr_level += 1
            elif ch == "*":  # \n
                curr_name: str = "".join(curr_str)

                if curr_level == 0:
                    level_0_node.add(curr_name)
                last_node_at_level[curr_level] = curr_name
                graph[last_node_at_level[curr_level]] = set()
                prev_level: int = curr_level - 1
                if prev_level >= 0:
                    graph[last_node_at_level[prev_level]].add(curr_name)

                curr_str = []
                curr_level = 0
            else:  # normal character => append it to curr_str
                curr_str.append(ch)
        if new_str[-1] != "*":
            curr_name: str = "".join(curr_str)

            if curr_level == 0:
                level_0_node.add(curr_name)

            last_node_at_level[curr_level] = curr_name
            graph[last_node_at_level[curr_level]] = set()
            prev_level: int = curr_level - 1
            if prev_level >= 0:
                graph[last_node_at_level[prev_level]].add(curr_name)

        for node in level_0_node:
            dfs(node, len(node))

        return ans
