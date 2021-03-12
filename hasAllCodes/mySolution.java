// link: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution {
    private HashMap<String, Boolean> stringWithLengthK = new HashMap<>();
    private boolean ans = true;
    
    void populateString(String s, int k) {
        if (!ans) return;
        
        if (s.length() == k) {
            ans = stringWithLengthK.containsKey(s);
        }
        else {
            populateString(s + "0", k);
            populateString(s + "1", k);
        }
    }
    
    public boolean hasAllCodes(String s, int k) {
        String substring = "";
        
        for (int index = 0; index <= s.length() - k; ++index) {
            substring = s.substring(index, index + k);
            if (!stringWithLengthK.containsKey(substring)) {
                stringWithLengthK.put(substring, true);
            }
        }
        
        populateString("", k);
        
        return ans;
    }
}