class Solution {
public:
    int maxPower(string s) {
        std::size_t start, end;
        int answer = 1, currentPower = 1;
        
        start = end = 0;
        
        while (end < s.length()) {
            if (s[end] != s[start]) {
                currentPower = end - start;
                if (currentPower > answer) {
                    answer = currentPower;
                }
                start = end;   
            }
            else if (end == s.length() - 1) {
                currentPower = end - start + 1;
                if (currentPower > answer) {
                    answer = currentPower;
                }
            }
            
            ++end;
        }
        
        return answer;
    }
};