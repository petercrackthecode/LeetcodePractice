class Solution {
public:
    string decodeString(string s) {
        string ans{""},
               expandedString{""};
        
        stack<int> bracketsStart;
        stack<int> duplicateTime;
        
        int position = 0,
            dupTime = 1;
    
        string currentNum = "";
        
        for (char ch : s) {
            if ('a' <= ch && ch <= 'z') {
                if (bracketsStart.empty())
                    ans += ch;
                else expandedString += ch;
            }
            else if ('0' <= ch && ch <= '9')
                currentNum += ch;
            else if (ch == '[') {
                duplicateTime.push(stoi(currentNum));
                currentNum = "";
                bracketsStart.push(expandedString.length());
            }
            else if (ch == ']') {
                position = bracketsStart.top(),
                dupTime = duplicateTime.top();
                
                bracketsStart.pop();
                duplicateTime.pop();
                
                string duplicateString = expandedString.substr(position);
                expandedString = expandedString.substr(0, position);
                
                while (dupTime > 0) {
                    expandedString += duplicateString;
                    --dupTime;
                }
                
                if (bracketsStart.empty()) {
                    ans += expandedString;
                    expandedString = "";
                }
            }            
        }
        
        return ans;
    }
};