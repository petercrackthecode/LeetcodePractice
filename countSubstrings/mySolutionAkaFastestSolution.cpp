// link: https://leetcode.com/problems/palindromic-substrings/
class Solution {
public:
    int countSubstrings(string s) {
        int ans = 0;
        for (int index = 0; index < s.size(); ++index) {
            int left = index,
                right = index;
            
            // span 1
            while ((left >= 0 && right < s.size()) && s[left] == s[right]) {
                ++ans;
                --left;
                ++right;
            }
            
            // span 2
            left = index;
            right = index + 1;
            while ((left >= 0 && right < s.size()) && s[left] == s[right]) {
                ++ans;
                --left;
                ++right;
            }
        }
        
        return ans;
    }
};