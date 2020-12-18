// link: https://leetcode.com/problems/increasing-triplet-subsequence/
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if (nums.size() < 3)
            return false;
        
        int smallestIndex = INT_MIN,
            secondSmallestIndex = INT_MIN;
        
        for (int index = 1; index < nums.size(); ++index) {
            if (nums[index] > nums[index - 1]) {
                if (smallestIndex == INT_MIN || secondSmallestIndex == INT_MIN) {
                    smallestIndex = index - 1;
                    secondSmallestIndex = index;
                }
                else { // smallestIndex & secondSmallestIndex are both initialized
                    if (nums[index] > nums[secondSmallestIndex] || nums[index - 1] > nums[smallestIndex])
                        return true;
                    else if (std::min(nums[secondSmallestIndex], nums[index]) == nums[index]) {
                        smallestIndex = index - 1;
                        secondSmallestIndex = index;
                    }
                }
            }
        }
        
        return false;
    }
};