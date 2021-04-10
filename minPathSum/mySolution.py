class Solution:
    def __init__(self):
        self.min_cost = dict({})
        
    def minPathRecursive(self, grid: List[List[int]], row, col) -> int:
        if (row, col) in self.min_cost:
            return self.min_cost[(row, col)]
        elif row == len(grid) - 1 and col == len(grid[0]) - 1:
            return grid[row][col]
        
        min_cost_right = sys.maxsize
        min_cost_bottom = sys.maxsize
        if col + 1 < len(grid[0]):
            min_cost_right = self.minPathRecursive(grid, row, col + 1) + grid[row][col]
        if row + 1 < len(grid):
            min_cost_bottom = self.minPathRecursive(grid, row + 1, col) + grid[row][col]
            
        self.min_cost[(row, col)] = min(min_cost_right, min_cost_bottom)
        
        return self.min_cost[(row, col)]
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
        row = 0
        col = 0
        
        self.min_cost[(row, col)] = sys.maxsize
        
        if col + 1 < len(grid[0]): # move right
            self.min_cost[(row, col)] = min(self.minPathRecursive(grid, row, col + 1) + grid[row][col], self.min_cost[(row, col)])
        if row + 1 < len(grid): # move right
            self.min_cost[(row, col)] = min(self.minPathRecursive(grid, row + 1, col) + grid[row][col], self.min_cost[(row, col)])
        
        
        return self.min_cost[(row, col)]
        