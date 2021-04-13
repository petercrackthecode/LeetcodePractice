class Solution {
public:
	int longestValidParentheses(string s) {
		int n = s.size();
		vector<int> dp(n, 0);

		int open = 0, ans = 0;
		for (int i = 0; i < n; ++i) {
			if (s[i] == '(') {
				++open;
				continue;
			}

			if (open == 0) continue;
			dp[i] = dp[i - 1] + 2;
			if (i - dp[i] >= 0) dp[i] += dp[i - dp[i]];
			--open;
			ans = max(ans, dp[i]);
		}

		return ans;
	}
}