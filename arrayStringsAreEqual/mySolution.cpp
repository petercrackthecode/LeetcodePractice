// link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        int indexOfWord1 = 0,
            indexOfWord2 = 0;
        
        int substringIndexOfWord1 = 0,
            substringIndexOfWord2 = 0;
        
        while (indexOfWord1 < word1.size() && indexOfWord2 < word2.size()) {
            if (word1[indexOfWord1][substringIndexOfWord1] != word2[indexOfWord2][substringIndexOfWord2])
                return false;
            else {
                if (substringIndexOfWord1 < word1[indexOfWord1].length() - 1) {
                    ++substringIndexOfWord1;
                }
                else {
                    ++indexOfWord1;
                    substringIndexOfWord1 = 0;
                }
                
                if (substringIndexOfWord2 < word2[indexOfWord2].length() - 1) {
                    ++substringIndexOfWord2;
                }
                else {
                    ++indexOfWord2;
                    substringIndexOfWord2 = 0;
                }
            }
        }
        
        if (indexOfWord1 < word1.size() || indexOfWord2 < word2.size())
            return false;
        
        return true;
    }
};