// link: https://leetcode.com/problems/vowel-spellchecker/
class Solution {   
    TrieNode root = new TrieNode();
    public String[] spellchecker(String[] wordlist, String[] queries) {
        String[] res = new String[queries.length];
        for (String word : wordlist) {
            insert(word);
        }
        for (int i = 0; i < queries.length; i++) {
            res[i] = query(queries[i]);
        }
        return res;
    }
    
    private void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if ("aeiouAEIOU".indexOf(c) != -1) {
                if (node.children[0] == null) {
                    node.children[0] = new TrieNode();
                }
                node = node.children[0];
            } else {
                c = Character.toLowerCase(c);
                if (node.children[c - 'a'] == null) {
                   node.children[c - 'a'] = new TrieNode();
                }
                node = node.children[c - 'a'];
            }
        }
        node.isEnd = true;
        node.list.add(word); // Store all words at the end node.
    }
    
    private String query(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if ("aeiouAEIOU".indexOf(c) != -1) {
                if (node.children[0] == null) return "";
                node = node.children[0];
            } else {
                c = Character.toLowerCase(c);
                if (node.children[c - 'a'] == null) return "";
                node = node.children[c - 'a'];
            }
        }
        if (node.isEnd == false) return "";   // If not end, return empty
        if (node.list.contains(word)) return word; // If list contains exactly the same word, return the word.
        
        String res = findCap(node.list, word); // Search for the first capitalized match
        if (res != "") return res;
      
        return node.list.get(0); // Return the first one that change vowels
    }
    
    private String findCap(List<String> list, String word) {
        for (String str : list) {
            if (str.toLowerCase().equals(word.toLowerCase())) return str;
        }
        return "";
    }
    
}

class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
    List<String> list = new ArrayList<>();
}