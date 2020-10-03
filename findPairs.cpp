// link: https://leetcode.com/problems/k-diff-pairs-in-an-array/
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        int ans = 0;
        std::map<int, int> numsFreq;
        
        for (auto num : nums)   {
            ++numsFreq[num];
        }
        
        for (auto numFreq : numsFreq)   {
            if (k == 0) {
                if (numFreq.second > 1)
                    ++ans;
            }
            else {
                int lowerBound = numFreq.first - k;
                if (numsFreq[lowerBound] != 0)  {
                    ++ans;
                }
            }
        }
        
        return ans;
    }
};          
