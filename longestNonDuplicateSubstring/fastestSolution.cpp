// link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
		vector<int> dict(256, -1);
        int maxLen = 0, start = -1;
        for (int i = 0; i != s.length(); i++) {
            if (dict[s[i]] > start)
                start = dict[s[i]];
            dict[s[i]] = i;
            maxLen = max(maxLen, i - start);
        }
        return maxLen;       
        
        /*
        
        Second attempt a few days later 
        
        
        int longestLength = 0;
        int windowStartIndex = 0;
        int windowEndIndex = 0;
        unordered_set<char> charsInWindow;
        
        while (windowEndIndex < s.size()){
            if (charsInWindow.find(s[windowEndIndex]) == charsInWindow.end()){
                charsInWindow.insert(s[windowEndIndex]);
                longestLength = max(longestLength, windowEndIndex - windowStartIndex + 1);
            } else {
                while (windowStartIndex < windowEndIndex){
                    if (s[windowStartIndex] == s[windowEndIndex]){
                        windowStartIndex++;
                        break;
                    } else {
                        charsInWindow.erase(s[windowStartIndex]);
                        windowStartIndex++;
                    }
                }
            }
            
            windowEndIndex++;
        }
        
        return max(longestLength, windowEndIndex - windowStartIndex);
        
        
        */
        
        /*
        if (s.length() == 0){
            return 0;
        }
        
        int lengthOfCurrentMax = 1;
        int substringStartIndex = 0;
        unordered_map<char, int> usedCharacters;
        
        for (int i=0; i<s.length(); i++){
            if (usedCharacters.find(s[i]) == usedCharacters.end()){
                usedCharacters.insert({s[i], i});
            } else {
                substringStartIndex = max(substringStartIndex, usedCharacters.find(s[i])->second + 1);
                usedCharacters[s[i]] = i;
            }
            
            lengthOfCurrentMax = max(lengthOfCurrentMax, i - substringStartIndex + 1);
        }
        
        return lengthOfCurrentMax;
        */
    }
};