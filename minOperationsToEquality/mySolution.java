// link: https://leetcode.com/problems/minimum-operations-to-make-array-equal/
class Solution {
    public int minOperations(int n) {
        int first = 0,
            second = 0;
        
        int ans = 0;
        
        for (int i = 0; i <= n/2; ++i) {
            first = second;
            second = i * 2 + 1;
        }
        
        if (n % 2 == 1)
            first = second;
        
        int avg = (first + second) / 2;
        
        for (int i = 0; i < n/2; ++i) {
            ans += avg - (i*2 + 1);
        }
        
        return ans;
    }
}