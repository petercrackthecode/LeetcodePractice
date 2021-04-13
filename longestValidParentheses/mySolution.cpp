class Solution {
    auto isUniformlyExpandable(const string &s, const int &left, const int &right) -> bool {
        return (left > 0 && right < s.size() - 1) && (s[left - 1] == '(' && s[right + 1] == ')');
    }
    
    auto isLeftSideExpandable(const vector<int> &start, const int &left) {
        return (left >= 2 && start[left - 1] != -1);
    }
public:
    int longestValidParentheses(string s) {
        if (s.size() < 2) // cannot form a pair of valid parentheses substring with less than 2 characters.
            return 0;
        // if i is the end position of a valid parentheses substring, start[i] is the start position of that group.
        vector<int> start(s.size(), -1);
        int ans = 0;
        
        // populate start
        for (int index = s.size() - 1; index > 0; --index) {
            if (s[index] == ')' && s[index - 1] == '(') {
                start[index] = index - 1;
                ans = 2;
            }
        }
        
        int right = 1;
        
        while (right < s.size()) {
            if (start[right] != -1) {
                bool isExpandable = false;
                int left = start[right];
                
                // expanding on both sides
                if (isUniformlyExpandable(s, left, right)) {
                    --left;
                    ++right;
                    start[right] = left;
                    isExpandable = true;
                }
                // check valid pairs on the left side
                if (isLeftSideExpandable(start, left)) {
                    left = start[left - 1];
                    start[right] = left;
                    isExpandable = true;
                }
                
                ans = std::max(ans, right - left + 1);
                
                if (!isExpandable)
                    ++right;
            }
            else ++right;
        }
        
        return ans;
    }
};