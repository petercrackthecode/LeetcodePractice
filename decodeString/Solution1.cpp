class Solution {
public:
    string decodeString(string s) {
        int i=0;
        return generate(s, i);
    }

private:
    string generate(string& s, int& i) {
        string result;
        while (i<s.size() && s[i] != ']') {
            if (!isdigit(s[i])) {
                result += s[i++];
            } else {
                int num=0;
                while (i<s.size() && isdigit(s[i]))
                    num = num*10 + (s[i++]-'0');
                
                i++;
                string temp = generate(s, i);
                i++;
                
                while (num--)
                    result += temp;
            }
        }
        return result;
    }
};