// link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cheapStock = INT_MAX;
        int ans = 0;
        
        for (int index = 0; index < prices.size(); ++index) {
            if (prices[index] <= cheapStock) {
                cheapStock = prices[index];
            }
            else {
                ans = std::max(ans, prices[index] - cheapStock);
            }
        }
        
        return ans;
    }
};