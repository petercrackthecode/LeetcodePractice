class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int ans = -1;
        
        map<int, int> rightSum,
                      leftSum;
        
        int remainder = x,
            currentSum = 0;
        
        int index = 0;
        
        // populate leftSum
        while (index < nums.size() && remainder >= nums[index]) {
            currentSum += nums[index];
            leftSum[currentSum] = index + 1;
            remainder -= nums[index];
            ++index;
        }
        
        currentSum = 0;
        remainder = x;
        index = nums.size() - 1;
        
        // populate leftSum
        while (index >= 0 && remainder >= nums[index]) {
            currentSum += nums[index];
            rightSum[currentSum] = nums.size() - index;
            remainder -= nums[index];
            --index;
        }
        
        remainder = x;
        index = 0;
        
        while (index < nums.size() && remainder >= nums[index]) {
            remainder -= nums[index];
            if (remainder == 0) {
                ans = (ans == -1) ? (index + 1) : std::min(ans, static_cast<int>(index + 1));
            }
            else if (rightSum.count(remainder) > 0 && index != nums.size() - rightSum[remainder]) {
                ans = (ans == -1) ? (rightSum[remainder] + index + 1) : std::min(ans, static_cast<int>(rightSum[remainder] + index + 1));
            }
            
            ++index;
        }
        
        remainder = x;
        index = nums.size() - 1;
        
        while (index >= 0 && remainder >= nums[index]) {
            remainder -= nums[index];
            if (remainder == 0) {
                ans = (ans == -1) ? (nums.size() - index) : std::min(ans, static_cast<int>(nums.size() - index));
            }
            else if (leftSum.count(remainder) > 0 && index + 1 != leftSum[remainder]) {
                ans = (ans == -1) ? (leftSum[remainder] + nums.size() - index) : std::min(ans, static_cast<int>(leftSum[remainder] + nums.size() - index));
            }
            
            --index;
        }
        
        return ans;
    }
};