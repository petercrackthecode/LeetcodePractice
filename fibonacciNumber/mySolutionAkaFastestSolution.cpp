// https://leetcode.com/problems/fibonacci-number/

class Solution {
    public int fib(int n) {
        int first = 0,
            second = 1,
            ans = 0;
        for (int i = 0; i <= n; ++i) {
            if (i == 0) {
                ans = first;
            }
            else if (i == 1)
                ans = second;
            else {
                ans = first + second;
                first = second;
                second = ans;
            }
        }
        
        return ans;
    }
}