// link: https://leetcode.com/problems/short-encoding-of-words/

class Solution {
    /*
        1. Initialize the string s with an empty string.
        2. Iterate through words:
            - If word[i] is found in s (using the indexOf method):
              + Take the substring from the found_position to the nearest # character, if
              the substr equals to word[i], do nothing.
              + Else keep searching using the indexOf at the next search Position (++searchStart);
            - else, append(word[i] + "#").
        3. Return the length of s.
    */
    
    private boolean shouldAppendNewString(String s, String substr) {
        if (s.length() == 0)
            return true;
        
        boolean foundValidSubstr = false;
        int searchStart = 0;
        int foundPosition = -1;
        
        while (!foundValidSubstr) {
            foundPosition = s.indexOf(substr, searchStart);
            if (foundPosition != -1) {
                // take the substring from searchStart to the next position of #
                if (s.charAt(foundPosition + substr.length()) == '#')
                    foundValidSubstr = true;
                else ++searchStart;
            }
            else break;
        }
        
        return !foundValidSubstr;
    }
    
    public int minimumLengthEncoding(String[] words) {
        String s = "";
        
        Arrays.sort(words, new Comparator<String>() {
           public int compare(String s1, String s2) {
               // sort descendingly based on strings' lengths
               return s2.length() - s1.length();
           } 
        });
        
        for (String word : words) {
            if (shouldAppendNewString(s, word)) {
                s += word + "#";
            }
        }
        
        return s.length();
    }
}