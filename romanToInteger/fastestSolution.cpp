// link: https://leetcode.com/problems/roman-to-integer/
class Solution {
    public int romanToInt(String s) {
        int sum = 0;
        
        int n = s.length();
        for (int i = n-1; i>=0; i--){
            char ch = s.charAt(i);
            switch (ch){
                case 'I': sum += sum>=5?-1: 1; break;
                case 'V': sum += 5;break;
                case 'X': sum += sum>=50?-10: 10;break;
                case 'L': sum += 50;break;
                case 'C': sum += sum>=500? -100: 100;break;
                case 'D': sum += 500;break;
                case 'M': sum += 1000;break;
                
            }
        }
        
        return sum;
    }
}