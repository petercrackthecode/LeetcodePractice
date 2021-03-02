// https://leetcode.com/problems/longest-palindromic-substring/

class Solution {
    private Boolean isPalindromic(String s) {
        for (int start = 0; start < s.length() / 2; ++start) {
            if (s.charAt(start) != s.charAt(s.length() - start - 1))
                return false;
        }
        
        return true;
    }
    
    public String longestPalindrome(String s) {
        int currentSubsequenceLength = s.length();
        String ans = "",
               potentialPalindrome = "";
        
        while (currentSubsequenceLength > 0 && ans.equals("")) {
            for (int start = 0; start <= s.length() - currentSubsequenceLength; ++start) {
                potentialPalindrome = s.substring(start, start + currentSubsequenceLength);
                if (isPalindromic(potentialPalindrome)) {
                    ans = potentialPalindrome;
                    break;
                }
            }
            
            --currentSubsequenceLength;
        }
        
        return ans;
    }
}