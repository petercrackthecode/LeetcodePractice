# https://leetcode.com/problems/number-of-islands/
from typing import List

class Solution:
    def __init__(self):
        self.number_of_islands = 0
        self.scanned_islands = set()
    
    def scan_nearby_islands(self, pos, grid) -> None:
        (row, col) = pos
        self.scanned_islands.add((row, col))

        if row > 0 and grid[row-1][col] == "1" and not (row-1, col) in self.scanned_islands:
            # top
            self.number_of_islands -= 1
            self.scan_nearby_islands((row-1, col), grid)
        if row < len(grid) - 1 and grid[row+1][col] == "1" and not (row+1, col) in self.scanned_islands:
            # bottom
            self.number_of_islands -= 1
            self.scan_nearby_islands((row+1, col), grid)
        if col > 0 and grid[row][col-1] == "1" and not (row, col-1) in self.scanned_islands:
            # left
            self.number_of_islands -= 1
            self.scan_nearby_islands((row, col-1), grid)
        if col < len(grid[0]) - 1 and grid[row][col+1] == '1' and not (row, col+1) in self.scanned_islands:
            # right
            self.number_of_islands -= 1
            self.scan_nearby_islands((row, col+1), grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        - read all the positions of the grid. Save all the positions of the cells with values == 1 to a set call island_positions(set of tuples).
        - set the number_of_islands = len(island_positions)
        - have a helper function called scan_nearby_island(pos) which takes in position and scan nearby pos.
        - have a set called scanned_islands to save the positions of the islands that we already checked.
        - iterate through island_positions: 
            for (row, col) in island_positions:
                if (row, col) in scanned_islands:
                    continue
                else:
                    scanned_islands.add((row, col))

        """
        island_positions = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    island_positions.add((row, col))

        self.number_of_islands = len(island_positions)

        for (row, col) in island_positions:
            if (row, col) in self.scanned_islands:
                continue
            else:
                self.scan_nearby_islands((row, col), grid)

        return self.number_of_islands
