// link: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
class Solution {
    public String findLongestWord(String s, List<String> d) {
        int len = s.length();
        
        int[][] indexes = new int[len + 1][26];
        
        Arrays.fill(indexes[len], Integer.MAX_VALUE);
        
        for (int i = len - 1; i >= 0; i--) {
            for (int j = 0; j < 26; j++) {
                indexes[i][j] = indexes[i + 1][j];
            }
            indexes[i][s.charAt(i) - 'a'] = i + 1;
        }
        
        String res = "";
        
        for (String word : d) {
            if (word.length() > s.length() || word.length() < res.length()) continue;
            int i = 0;
            int j = 0;
            
            while (j < word.length()) {
                char c = word.charAt(j);
                if (indexes[i][c - 'a'] == Integer.MAX_VALUE) break;
                i = indexes[i][c - 'a'];
                j++;
            }
            
            if (j == word.length()) {
                if (word.length() > res.length() || word.length() == res.length() && word.compareTo(res) < 0) {
                    res = word;
                }
            }
        }
        
        return res;
    }
}