// link: https://leetcode.com/problems/roman-to-integer/
class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> symbolToValue = new HashMap<Character, Integer>();
        
        symbolToValue.put('I', 1);
        symbolToValue.put('V', 5);
        symbolToValue.put('X', 10);
        symbolToValue.put('L', 50);
        symbolToValue.put('C', 100);
        symbolToValue.put('D', 500);
        symbolToValue.put('M', 1000);
        
        int ans = 0;
        
        for (int index = 0; index < s.length(); ++index) {
            if (index > 0 && symbolToValue.get(s.charAt(index - 1)) < symbolToValue.get(s.charAt(index))) {
                ans -= (symbolToValue.get(s.charAt(index - 1)) * 2);
            }
            
            ans += symbolToValue.get(s.charAt(index));
        }
        
        return ans;
    }
}