// link: https://leetcode.com/problems/short-encoding-of-words/



class Solution {
    class Trie {
        Trie[] next = null;
    }
    

    private int visit(String s, Trie node) {
        boolean newBranch = false;
        int created = 0, length = s.length();
        for (int i = length - 1; i >= 0; i--) {   
            boolean newLevel = false;
            int idx = s.charAt(i) - 'a';
            if (null == node.next) {
                newLevel = true;
                node.next = new Trie[26];
            }

            if (null == node.next[idx])  {
                if (!newLevel) newBranch = true;
                node.next[idx] = new Trie();
                created++;
            }            
            node = node.next[idx];
        }

        return newBranch ? length + 1 : created;
    }
    
    public int minimumLengthEncoding(String[] words) {
        Trie root = new Trie();
        root.next = new Trie[26];
        int ret = 0;
        for (String s:words) {
            ret += visit(s, root);
        }
        return ret;
    }
}
