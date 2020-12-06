// link: https://leetcode.com/problems/can-place-flowers/
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int plantsLeftToPlot = n;
        
        // check with odd indices first
        int index = 1;
        while (plantsLeftToPlot > 0 && index < flowerbed.size()) {
            if (flowerbed[index] == 0) {
                if (index == flowerbed.size() - 1) {
                    if (flowerbed[index - 1] == 0)
                        --plantsLeftToPlot;
                }
                else if (flowerbed[index - 1] == 0 && flowerbed[index + 1] == 0) {
                    --plantsLeftToPlot;
                }
            }
            
            index += 2;
        }
        
        if (plantsLeftToPlot == 0)
            return true;
        
        // check with the even indices
        plantsLeftToPlot = n;
        index = 0;
        
        while (plantsLeftToPlot > 0 && index < flowerbed.size()) {
            if (flowerbed[index] == 0) {
                if (index == 0 && index == flowerbed.size() - 1) {
                    --plantsLeftToPlot;
                }
                else if (index == 0) { // index != floweredbed.size() - 1
                    if (flowerbed[index + 1] == 0)
                        --plantsLeftToPlot;
                }
                else if (index == flowerbed.size() - 1) { // index != 0
                    if (flowerbed[index - 1] == 0)
                        --plantsLeftToPlot;
                }
                else if (flowerbed[index - 1] == 0 && flowerbed[index + 1] == 0)
                    --plantsLeftToPlot;
            }
            
            index += 2;
        }
        
        if (plantsLeftToPlot == 0)
            return true;
        
        return false;
    }
};