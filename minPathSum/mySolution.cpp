typedef std::pair<int, int> pii;
typedef vector<vector<int>> vvi;
class Solution {
    private:
        map<pii, int> minCost;
public:
    auto minPathRecursive(const vvi &grid, const int &row, const int &col) -> int {
        if (minCost.count(make_pair(row, col)))
            return minCost[make_pair(row, col)];
        if (row == grid.size() - 1 && col == grid[0].size() - 1)
            return grid[row][col];
        
        
        int minCostRight = INT_MAX,
            minCostBottom = INT_MAX;
        if (col + 1 < grid[0].size())
            minCostRight = minPathRecursive(grid, row, col + 1) + grid[row][col];
        if (row + 1 < grid.size())
            minCostBottom = minPathRecursive(grid, row + 1, col) + grid[row][col];
        
        minCost[make_pair(row, col)] = std::min(minCostRight, minCostBottom);
        
        return minCost[make_pair(row, col)];
    }
    
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.size() == 1 && grid[0].size() == 1)
            return grid[0][0];
        
        minCost[make_pair(0, 0)] = INT_MAX;
        
        int row = 0,
            col = 0;
        
        if (col + 1 < grid[0].size()) // move right
            minCost[make_pair(row, col)] = min(minPathRecursive(grid, row, col + 1) + grid[row][col], minCost[make_pair(row, col)]);
        // move bottom
        if (row + 1 < grid.size()) // move bottom
            minCost[make_pair(row, col)] = min(minPathRecursive(grid, row + 1, col) + grid[row][col], minCost[make_pair(row, col)]);
        
        return minCost[make_pair(row, col)];
    }
};