// link: https://leetcode.com/problems/non-decreasing-array/
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        bool didModify{false};
        
        for (int i = 0; i < int(nums.size()) - 2; ++i) {
            if (nums[i] > nums[i+1] && nums[i+1] > nums[i+2])
                return false;
            else if (nums[i] <= nums[i+1] && nums[i+1] > nums[i+2]) {
                if (didModify)
                    return false;
                
                if (nums[i] > nums[i+2])
                    nums[i+2] = nums[i+1];
                else nums[i+1] = nums[i+2];
                
                didModify = true;
            }
            else if (nums[i] > nums[i+1] && nums[i+1] <= nums[i+2]) {
                nums[i] = nums[i+1];
                didModify = true;
            }
        }
        
        return true;
    }
};