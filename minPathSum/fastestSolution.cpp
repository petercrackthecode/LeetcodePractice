class Solution {
public:
	int minPathSum(vector<vector<int>> &grid) {
		// Fast I/O in C++
		ios_base::sync_with_stdio(false);
		cin.tie(NULL);

		int rows = grid.size();
		if (rows == 0)
			return 0;
		int cols = grid[0].size();
		vector<vector<int>> dp(rows, vector<int>(cols, 0));
		int i, j;

		dp[0][0] = grid[0][0]; // 1st element is the starting point
		// Fill in the 1st row
		for (i = 1; i < cols; ++i)
			dp[0][i] = dp[0][i - 1] + grid[0][i];

		// Fill in the 1st col
		for (i = 1; i < rows; ++i) {
			for (j = 1; j < cols; ++j)
				dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j-1]);
		}

		return dp[rows - 1][col - 1];
	}
};