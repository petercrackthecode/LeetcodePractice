// link: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
class Solution {
    private static Boolean canFormSubsequence(String s, String substr) {
        int sIndex = 0,
            substrIndex = 0;
        
        while (substrIndex < substr.length() && sIndex < s.length()) {
            if (substr.charAt(substrIndex) == s.charAt(sIndex)) {
                ++substrIndex;
            }
            
            ++sIndex;
        }
        
        return substrIndex == substr.length();
    }
    
    public String findLongestWord(String s, List<String> d) {
        String longestWord = "";
        
        for (String str : d) {
            if (str.length() < longestWord.length())
                continue;
            else if (canFormSubsequence(s, str)) {
                if (longestWord.length() < str.length())
                    longestWord = str;
                else if (longestWord.length() == str.length()) {
                    longestWord = longestWord.compareTo(str) > 0 ? str : longestWord;
                }
            }
        }
        
        return longestWord;
    }
}