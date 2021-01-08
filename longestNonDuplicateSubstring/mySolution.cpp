// link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() <= 1)
            return s.length();
        
        std::map<char, int> charactersFrequency;
        
        unsigned int subStringStart = 0, 
                     subStringEnd = 1,
                     answer = 1;
        
        ++charactersFrequency[s[subStringStart]];
        ++charactersFrequency[s[subStringEnd]];
        
        while (subStringEnd < s.length()) {
            while (subStringStart < subStringEnd && charactersFrequency[s[subStringEnd]] > 1) {
                --charactersFrequency[s[subStringStart]];
                ++subStringStart;
            }
            
            answer = max(answer, subStringEnd - subStringStart + 1);
            ++subStringEnd;
            ++charactersFrequency[s[subStringEnd]];
        }
        
        return answer;
    }
};