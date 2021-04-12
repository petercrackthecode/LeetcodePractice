// link: https://leetcode.com/problems/verifying-an-alien-dictionary/submissions/
class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        int charOrder[26];
        for (int index= 0; index < order.size(); ++index) {
            charOrder[order[index] - 'a'] = index;
        }
        
        const vector<string> initial = words;
        std::sort(words.begin(), words.end(), [charOrder] (const string &a, const string &b) -> bool {
            const int shorterLength = (a.size() > b.size()) ? b.size() : a.size();
            for (int index = 0; index < shorterLength; ++index) {
                if (a[index] != b[index]) {
                    return charOrder[a[index] - 'a'] < charOrder[b[index] - 'a'];
                    // if true, a goes first. Else b goes first.
                }
            }

            // one string is the substring of another string
            return a.size() < b.size();
        });
        
        return initial == words;
    }
};