// link: https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode {
public:
    char character = ' ';
    map<char, TrieNode> children;
    
    TrieNode() {
        character = ' ';
    }
    
    TrieNode(char ch, map<char, TrieNode> _children) : character{ch}, children{_children} {
    }
};

class Trie {
private:
    map<char, TrieNode> trie;
public:
    /** Initialize your data structure here. */
    Trie() {
        
    }
    
    // We use the space character as the character to mark the end of a string
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        map<char, TrieNode> * temp = &trie;
        
        for (char ch : word) {
            if (temp->count(ch) == 0)
                (*temp)[ch] = TrieNode();
            temp = &(*temp)[ch].children;
        }
        
        (*temp)['\0'] = TrieNode();
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        map<char, TrieNode> * temp = &trie;
        
        for (char ch : word) {
            if (temp->count(ch) == 0)
                return false;
            temp = &(*temp)[ch].children;
        }
        
        return temp->count('\0') != 0;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        map<char, TrieNode> * temp = &trie;
        
        for (char ch : prefix) {
            if (temp->count(ch) == 0)
                return false;
            temp = &(*temp)[ch].children;
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