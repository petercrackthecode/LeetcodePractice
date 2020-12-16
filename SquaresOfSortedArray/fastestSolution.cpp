// link: https://leetcode.com/problems/squares-of-a-sorted-array/
vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        
        vector<int> res(n);
        int l = 0;
        int r = n-1;
        int k = n-1;
        int ll = nums[l] * nums[l];
        int rr = nums[r] * nums[r];
        while(l <= r) {
            if (ll > rr) {
                res[k] = ll;
                if (++l <= r) {
                    ll = nums[l] * nums[l];
                }
            } else {
                res[k] = rr;
                if (--r >= l) {
                    rr = nums[r] * nums[r];
                }
            }
            k--;
        }
        
        return res;
    }
    
    vector<int> sortedSquares_binary_search(vector<int>& nums) {
        int n = nums.size();
        const auto itr = lower_bound(nums.begin(), nums.end(), 0);
        int m = distance(nums.begin(), itr);
        
        for(int i = 0; i < nums.size(); ++i) {
            nums[i] *= nums[i];
        }
        
        vector<int> res(n);
        int i = m-1;
        int j = m;
        int k = 0;
        while(i >= 0 && j < n) {
            if (nums[i] < nums[j]) {
                res[k] = nums[i];
                i--;
            } else {
                res[k] = nums[j];
                j++;
            }
            k++;
        }
        
        while(i >= 0) {
            res[k++] = nums[i--];
        }
        
        while(j < n) {
            res[k++] = nums[j++];
        }
        
        return res;
    }