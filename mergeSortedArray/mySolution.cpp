class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        while (n > 0) {
            nums1[m] = nums2[n - 1];
            ++m;
            --n;
        }
        
        std::sort(nums1.begin(), nums1.end());
    }
};