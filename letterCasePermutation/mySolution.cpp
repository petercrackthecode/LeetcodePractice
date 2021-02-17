// link: https://leetcode.com/problems/letter-case-permutation/
class Solution {
    /*
        1.  Form a string to add to the list.
            Traverse through the String characters, each time when you see a character, check if it's a letter or not. If yes, we have two possibilities and we have to add an uppercase or lowercase to the member string. Otherwise, just add the current character to the member string.
        2.  Move on to the next character if there is more. Else, add the current member string to the list.
        
        Hint: Have a recursive function.
    */
    
    public static void getStringPermutation(List<String> list, String s, int currentIndex, String permutation) {
        if (currentIndex >= s.length() - 1) {
            list.add(permutation);
            return;
        }
        
        if (Character.isDigit(s.charAt(currentIndex + 1))) {
            getStringPermutation(list, s, currentIndex + 1, permutation + s.charAt(currentIndex + 1));
        }
        else {
            Character lower = Character.toLowerCase(s.charAt(currentIndex + 1)),
                      upper = Character.toUpperCase(s.charAt(currentIndex + 1));
            getStringPermutation(list, s, currentIndex + 1, permutation + lower);
            getStringPermutation(list, s, currentIndex + 1, permutation + upper);
        }
    }
    
    public List<String> letterCasePermutation(String S) {
        List<String> ans = new ArrayList<String>();
        
        if (Character.isDigit(S.charAt(0))) {
            getStringPermutation(ans, S, 0, String.valueOf(S.charAt(0)));
        }
        else {
            getStringPermutation(ans, S, 0, String.valueOf(Character.toLowerCase(S.charAt(0))));
            getStringPermutation(ans, S, 0, String.valueOf(Character.toUpperCase(S.charAt(0))));
        }
        
        return ans;
    }
}