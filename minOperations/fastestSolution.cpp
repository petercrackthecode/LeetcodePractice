auto speedup = []() {
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return nullptr;
}();

class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int sum=0;
        int l=0;
        for(;l<nums.size()&&sum<x;++l) {
            sum+=nums[l];
        }
        if(sum<x) {
            return -1;
        }
        int ans=-1;
        if(sum==x) {
            ans=l;
        }
        --l;
        int r=nums.size()-1;
        for(;l>=0;--l) {
            sum-=nums[l];
            for(;r>l&&sum<x;--r) {
                sum+=nums[r];
            }
            if(sum==x) {
                int tmp=l+(nums.size()-r-1);
                if(ans==-1||ans>tmp) {
                    ans=tmp;
                }
            }
        }
        return ans;
    }
};