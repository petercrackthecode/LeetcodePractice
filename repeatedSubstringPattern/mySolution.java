// https://leetcode.com/problems/repeated-substring-pattern/

class Solution {
    private boolean isSubstringRepeated(String substr, String s) {
        if (s.length() % substr.length() != 0)
            return false;
        
        int substrIndex = 0,
            sIndex = substr.length();
        while (sIndex < s.length()) {
            if (substr.charAt(substrIndex) != s.charAt(sIndex))
                return false;
            
            substrIndex = (substrIndex + 1) % substr.length();
            ++sIndex;
        }
        
        return true;
    }
    
    public boolean repeatedSubstringPattern(String s) {
        String substr = s.substring(0, 1);
        
        while (substr.length() <= s.length() / 2) {
            if (isSubstringRepeated(substr, s))
                return true;
            substr += s.charAt(substr.length());
        }
        
        return false;
    }
}