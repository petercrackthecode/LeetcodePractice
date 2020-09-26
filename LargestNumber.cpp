class Solution {
public:
    static bool sortString(std::string first, std::string second)  {
        return first + second > second + first;
    }
    
    string largestNumber(vector<int>& nums) {
        std::vector<std::string> strNums;
        bool isAllZeroes = true;
        
        for (auto num :  nums)  {
            if (num != 0) 
                isAllZeroes = false;
            strNums.push_back(std::to_string(num));
        }
        
        if (isAllZeroes) return "0";
        
        std::sort(strNums.begin(), strNums.end(), sortString);
        
        std::string ans{""};
        
        for (auto strNum : strNums) {
            ans += strNum;
        }
        
        return ans;
    }
};