// link: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
#include <limits.h> // for INT_MIN and INT_MAX
#include <cstddef>
#include <cmath>
#include <algorithm>

class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int minCost = INT_MAX,
            currentCost = 0;
        
        for (std::size_t index = 0; index < position.size(); ++index) {
            // assume that we would move all the chips to the index position;
            currentCost = 0;
            for (int anotherIndex = 0; anotherIndex < position.size(); ++anotherIndex) {
                if (anotherIndex != index) {
                    if (std::abs(position[index] - position[anotherIndex]) % 2 == 1) {
                        ++currentCost;
                    }
                }
            }
            
            minCost = std::min(minCost, currentCost);
        }
        
        return minCost;
    }
};