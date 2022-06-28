# https://leetcode.com/problems/flood-fill
from typing import List


class Solution:
    def recursiveFloodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int, old_color: int) -> List[List[int]]:
        # Fill the pixel with the new color
        image[sr][sc] = new_color

        # top
        if sr - 1 >= 0 and image[sr - 1][sc] == old_color:
            self.recursiveFloodFill(image, sr - 1, sc, new_color, old_color)
        # bottom
        if sr + 1 < len(image) and image[sr + 1][sc] == old_color:
            self.recursiveFloodFill(image, sr + 1, sc, new_color, old_color)
        # left
        if sc - 1 >= 0 and image[sr][sc - 1] == old_color:
            self.recursiveFloodFill(image, sr, sc - 1, new_color, old_color)
        # right
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == old_color:
            self.recursiveFloodFill(image, sr, sc + 1, new_color, old_color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        old_color = image[sr][sc]
        # Fill the pixel with the new color
        image[sr][sc] = color

        # top
        if sr - 1 >= 0 and image[sr - 1][sc] == old_color:
            self.recursiveFloodFill(image, sr - 1, sc, color, old_color)
        # bottom
        if sr + 1 < len(image) and image[sr + 1][sc] == old_color:
            self.recursiveFloodFill(image, sr + 1, sc, color, old_color)
        # left
        if sc - 1 >= 0 and image[sr][sc - 1] == old_color:
            self.recursiveFloodFill(image, sr, sc - 1, color, old_color)
        # right
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == old_color:
            self.recursiveFloodFill(image, sr, sc + 1, color, old_color)

        return image
