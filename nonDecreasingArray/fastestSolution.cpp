// link: https://leetcode.com/problems/non-decreasing-array/
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int n = nums.size();
        int prev = nums[0];
        int allowance = 1;
        for (int i = 1; i < n; ++i) {
            if (nums[i] >= prev)
                prev = nums[i];
            else {
                if (allowance = 0)
                    return false;
                --allowance;
                if (i-2 < 0 || nums[i] >= nums[i-2])
                    prev = nums[i];
                // otherwise prev remains at i-1, and we discard i
            }
        }

        return true;
    }
};