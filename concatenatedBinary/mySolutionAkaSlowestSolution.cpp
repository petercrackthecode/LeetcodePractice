// link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution {
private:
    const int mod = static_cast<int>(1e9 + 7);
public:
    static auto addOneToBinaryNum(string &binary) -> void {
        if (binary == "")
            binary += "1";
        else {
            bool isOneCarryOn = false;
            
            if (binary[binary.length() - 1] == '1') {
                binary[binary.length() - 1] = '0';
                isOneCarryOn = true;
                
                int index = binary.length() - 2;
                
                while (index >= 0 && isOneCarryOn) {
                    if (binary[index] == '0') {
                        binary[index] = '1';
                        isOneCarryOn = false;
                    }
                    else {
                        binary[index] = '0';
                    }
                    
                    --index;
                }
                
                if (isOneCarryOn)
                    binary = '1' + binary;
            }
            else {
                binary[binary.length() - 1] = '1';
            }
        }
    }
    
    auto translateBinaryToDecimalAndAddToAnswer(const string &binary, int &ans) -> void {
        for (char ch : binary) {
            ans = (ans * 2) % mod;
            ans += (ch == '0') ? 0 : 1;
        }
    }
    
    int concatenatedBinary(int n) {
        int ans = 0;
        
        string currentDecimalValue = "";
        
        for (int num = 1; num <= n; ++num) {
            addOneToBinaryNum(currentDecimalValue);
            translateBinaryToDecimalAndAddToAnswer(currentDecimalValue, ans);
        }
        
        return ans;
    }
};