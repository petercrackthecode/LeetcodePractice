// link: https://leetcode.com/problems/count-binary-substrings/
class Solution {
    
    /*
        This problem is a variation of the palindromic substr problem.
        Insight: keep in mind that regardless of a valid substring's size, its length is an even number.
        Hence, we can start from the minimalistic version of all the valid substring: a valid substring with length 2, and keep expanding them as long as the left bound is the same character as the left core (i) and the right bound is the same character as the right core (j).
        Every time we expanding them and get a valid substring, increment ans by one.
        To get the valid substrings with length 2, scan all the substring with length 2, and take all the valid ones (s[i] != s[i + 1])
    */
public:
    int countBinarySubstrings(string s) {        
        int ans = 0;
        int left, right;
        for (int i = 0; i < s.size() - 1; ++i) {
            if (s[i] != s[i+1]) {
                left = i, right = i+1;
                
                while ((left >= 0 && right < s.size()) && (s[left] == s[i] && s[right] == s[i+1])) {
                    ++ans;
                    --left;
                    ++right;
                }
            }
        }
        
        
        return ans;
    }
};