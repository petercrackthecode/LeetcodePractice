// link: https://leetcode.com/problems/beautiful-arrangement-ii/
class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> ans;
        
        if (k == 1) {
            for (int num = 1; num <= n; ++num)
                ans.push_back(num);
        }
        else {
            int left = 1,
                right = n;
            bool addRightNext = false;
            
            while (k > 1) {
                if (k > 1) {
                    if (!ans.empty()) --k;
                    ans.push_back(left);
                    ++left;
                    addRightNext = true;
                }
                if (k > 1) {
                    ans.push_back(right);
                    --right;
                    --k;
                    addRightNext = false;
                }
            }
            
            // if addRightNext = true, add numbers from left -> right. Else add numbers from right -> left;
            if (addRightNext) {
                for (int num = left; num <= right; ++num)
                    ans.push_back(num);
            }
            else {
                for (int num = right; num >= left; --num)
                    ans.push_back(num);
            }
        }
        
        return ans;
    }
};