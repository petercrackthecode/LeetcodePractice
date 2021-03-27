// link: https://leetcode.com/problems/word-subsets/
class Solution {
public:        
        
    vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
        int hash[26] = {};
        
        for (const auto& b : B) {
            int subHash[26] = {};
            for (char ch : b) {
                char idx = ch - 'a';
                subHash[idx]++;
                hash[idx] = max(subHash[idx], hash[idx]);
            }
        }
        
        vector<string> result;
        for (const auto& a : A) {
            int subHash[26] = {};
            for (char ch : a) {
                subHash[ch - 'a']++;
            }
            
            bool isUniversal = true;
            for (char i = 0; i < 26; i++) {
                if (hash[i] > subHash[i]) {
                    isUniversal = false;
                    break;
                }
            }
            
            if (isUniversal) {
                result.push_back(a);
            }
        }
        return result;
    }
};