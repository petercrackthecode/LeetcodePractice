// link: https://leetcode.com/problems/beautiful-arrangement/

class Solution {
public:
    int countArrangement(int n, uint16_t chosen = 0, int size = 1) {
        if (size > n) return 1;
        int res = 0;
        for (int i = 1; i <= n; i++) {
            if (!(chosen & (1 << i)) && (!(i%size) || !(size%i))) {
                res += countArrangement(n, chosen | (1<<i), size+1);
            }
        }
        return res;
    }
};