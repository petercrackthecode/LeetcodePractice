// link: https://leetcode.com/problems/partition-equal-subset-sum/
#include <vector>

using namespace std;

class Solution
{
private:
    // -1 == haven't initialize
    //  0 == cannot form the sum
    //  1 == can form the sum
    vector<vector<int>> dp;

    auto canPartitionHelper(const vector<int> &nums, const int &sum, const int &index) -> bool
    {
        if (sum == 0)
            return true;
        else if (index >= nums.size() || sum < 0)
            return false;

        if (dp[sum][index] != -1)
            return dp[sum][index];

        bool skipElementAtIndex = canPartitionHelper(nums, sum, index + 1),
             takeElementAtIndex = canPartitionHelper(nums, sum - nums[index], index + 1);

        dp[sum][index] = (skipElementAtIndex || takeElementAtIndex);

        return dp[sum][index];
    }

public:
    bool canPartition(vector<int> &nums)
    {
        if (nums.size() < 2)
            return false;

        int sum = 0;
        int max = INT_MIN;
        for (auto num : nums)
        {
            sum += num;
            max = std::max(max, num);
        }

        if (sum % 2 != 0)
            return false;

        int half = sum / 2;

        vector<int> defaultVal(nums.size() + 1, -1);

        for (int i = 0; i < nums.size() * max + 1; ++i)
            dp.push_back(defaultVal);

        for (int i = 0; i < nums.size() * max + 1; ++i)
        {
            for (int j = 0; j < nums.size() + 1; ++j)
                dp[i][j] = -1;
        }

        bool skipElement0 = canPartitionHelper(nums, half, 1);
        bool takeElement0 = canPartitionHelper(nums, half - nums[0], 1);

        return skipElement0 || takeElement0;
    }
};