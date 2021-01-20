class Solution {
public:
    bool isValid(string s) {
        std::stack<char> openingBrackets;
        map<char, char> translateCloseBracketsToOpenBrackets;
        
        translateCloseBracketsToOpenBrackets[')'] = '('; 
        translateCloseBracketsToOpenBrackets['}'] = '{'; 
        translateCloseBracketsToOpenBrackets[']'] = '['; 
        
        for (char ch : s) {
            if (ch == '(' || ch == '{' || ch == '[') {
                openingBrackets.push(ch);
            }
            else {
                if (openingBrackets.empty() || translateCloseBracketsToOpenBrackets[ch] != openingBrackets.top())
                    return false;
                
                openingBrackets.pop();
            }
        }
        
        return openingBrackets.empty();
    }
};