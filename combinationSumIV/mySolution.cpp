// link: https://leetcode.com/problems/combination-sum-iv/
class Solution {
    std::map < int, int > waysToAddUpToNum;
    auto combinationSum4Recursive(const vector < int > & nums,
        const int & target) -> int {
        if (waysToAddUpToNum.count(target) == 0) {
            for (int i = 0; i < nums.size(); ++i) {
                if (target - nums[i] >= 0) {
                    waysToAddUpToNum[target] += combinationSum4Recursive(nums, target - nums[i]);
                } else break;
            }
        }

        return waysToAddUpToNum[target];
    }

public:
    int combinationSum4(vector < int > & nums, int target) {
        waysToAddUpToNum[0] = 1;
        std::sort(nums.begin(), nums.end());

        for (int index = 0; index < nums.size(); ++index) {
            if (target - nums[index] >= 0) {
                waysToAddUpToNum[target] += combinationSum4Recursive(nums, target - nums[index]);
            } 
            else break;
        }

        return waysToAddUpToNum[target];
    }
};