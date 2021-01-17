class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n <= 1)
            return n;
        else {
            int ans = INT_MIN;
            vector<int> nums(n+1, 0);
            nums[0] = 0;
            nums[1] = 1;
            
            for (int index = 2; index <= n; ++index) {
                if (index % 2 == 0)
                    nums[index] = nums[index / 2];
                else nums[index] = nums[index / 2] + nums[index / 2 + 1];
                
                ans = max(ans, nums[index]);
            }
            
            return ans;
        }
    }
};