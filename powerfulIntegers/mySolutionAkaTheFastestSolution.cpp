// link: https://leetcode.com/problems/powerful-integers/
class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        std::unordered_map<int, bool> hasNumberAppeared;
        int i = 0, j = 0;
        
        int xPow = 1, yPow;
        
        while (xPow + 1 <= bound) {
            yPow = 1;
            
            while (xPow + yPow <= bound) {
                int sum = xPow + yPow;
                if (hasNumberAppeared.count(sum) == 0)
                    hasNumberAppeared[sum] = true;
                
                if (y == 1)
                    break;
                yPow *= y;
            }
            
            if (x == 1)
                break;
            xPow *= x;
        }
        
        vector<int> ans;
        
        for (auto const& [key, val] : hasNumberAppeared) {
            ans.push_back(key);
        }
        
        return ans;
    }
};