// link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
class Solution {
public:
    string removeDuplicates(string s, int k) {
        std::stack<int> duplicateSequenceLength;
        std::stack<char> characters;
        int newDuplicateSequenceLength = 1;
        
        for (auto ch : s) {
            // characters and duplicateSequenceLength will share the same length
            int newDuplicateSequenceLength = 0;
            if (duplicateSequenceLength.empty() || characters.top() != ch) {
                newDuplicateSequenceLength = 1;
            }
            else {
                newDuplicateSequenceLength = duplicateSequenceLength.top() + 1;
            }
            
            duplicateSequenceLength.push(newDuplicateSequenceLength);
            characters.push(ch);
            
            if (newDuplicateSequenceLength == k) {
                for (int time = 0; time < k; ++time) {
                    duplicateSequenceLength.pop();
                    characters.pop();
                }
            }
        }
        
        string ans{""};
        
        while (!characters.empty()) {
            ans = characters.top() + ans;
            characters.pop();
        }
        
        return ans;
    }
};