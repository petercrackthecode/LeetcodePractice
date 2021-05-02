// link: https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode {
public:
    bool isWord;
    TrieNode* children[26];
    TrieNode()
    {
        this->isWord = false;
        for(int i=0;i<26;i++)
            this->children[i]= NULL;
    }
};


class Trie {
public:
    /** Initialize your data structure here. */
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* trav = root;
        for(char c: word)
        {
            if(trav->children[c-'a']==NULL)
                trav->children[c-'a'] = new TrieNode();
            trav = trav->children[c-'a'];
        }
        trav->isWord = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* trav = root;
        
        for(char c: word)
        {
            int idx = c-'a';
            if(trav->children[idx]==NULL)
                return false;
            trav = trav->children[idx];
        }
        return trav->isWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode* trav = root;
        
        for(char c: prefix)
        {
            int idx = c-'a';
            if(trav->children[idx]==NULL)
                return false;
            trav = trav->children[idx];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

