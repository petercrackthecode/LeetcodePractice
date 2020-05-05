// link: https://leetcode.com/problems/ransom-note/
bool canConstruct(string ransomNote, string magazine) {
        std::map<char, int> lettersMap;
        
        for (char ch : magazine) {
            ++lettersMap[ch];
        }
        
        for (char ch : ransomNote) {
            if (lettersMap[ch] > 0) {
                --lettersMap[ch];
            }
            else return false;
        }
        
        return true;
    }