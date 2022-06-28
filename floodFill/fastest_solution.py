# https://leetcode.com/problems/flood-fill
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r-1, c)
                if r+1 < R:
                    dfs(r+1, c)
                if c >= 1:
                    dfs(r, c-1)
                if c+1 < C:
                    dfs(r, c+1)

        dfs(sr, sc)
        return image


""" Tips learned: When ever you need to call a helper function,
    defined an inner function and call it instead of defining a member function for the class.
    That way, you don't have to use the self keyword when you call the function and your inner function has access to all
    variables outside of its inner scope """
