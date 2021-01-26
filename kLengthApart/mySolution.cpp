class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        bool isThisTheFirstNumber1 = true;
        int zeroesCount{0};
        
        for (int index = 0; index < nums.size(); ++index) {
            if (nums[index] == 1) {
                if (isThisTheFirstNumber1) {
                    isThisTheFirstNumber1 = false;
                }
                else if (zeroesCount >= k) {
                    zeroesCount = 0;
                }
                else return false;
            }
            else if (!isThisTheFirstNumber1) {
                ++zeroesCount;
            }
        }
        
        return true;
    }
};