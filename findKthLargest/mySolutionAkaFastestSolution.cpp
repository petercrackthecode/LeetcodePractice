class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end(), [=](const int &first, const int &second) -> bool {
            return first > second;
        });
        
        return nums[k-1];
    }
};