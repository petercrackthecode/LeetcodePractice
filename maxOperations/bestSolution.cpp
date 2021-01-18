// link: https://leetcode.com/problems/max-number-of-k-sum-pairs/
static const int _ = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int start=0,end=nums.size()-1,ans=0;
        while(start<end){
            int sum=nums[start]+nums[end];
            if(sum==k){
                ans++;
                start++;
                end--;
            }
            else if(sum>k){
                end--;
            }
            else{
                start++;
            }
        }
        return ans;
      
    }
};