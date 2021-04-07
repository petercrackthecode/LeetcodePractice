// link: https://leetcode.com/problems/determine-if-string-halves-are-alike/
class Solution {
    private boolean isVowel(char ch) {
        switch (Character.toUpperCase(ch)) {
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
                return true;
        }    
        
        return false;
    }
    
    public boolean halvesAreAlike(String s) {
        int leftPointer = 0;
        int leftHalfVowelsCount = 0,
            rightHalfVowelsCount = 0;
        
        while (leftPointer < s.length()/2) {
            if (isVowel(s.charAt(leftPointer)))
                ++leftHalfVowelsCount;
            if (isVowel(s.charAt(s.length() - 1 - leftPointer)))
                ++rightHalfVowelsCount;
                
                
            ++leftPointer;
        }
        
        return leftHalfVowelsCount == rightHalfVowelsCount;
    }
}