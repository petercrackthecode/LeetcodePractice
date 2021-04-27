// link: https://leetcode.com/problems/furthest-building-you-can-reach/
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        if (ladders <= 0) {
            int i;
            for (i = 0; i < heights.size() - 1; ++i) {    
                int heightDiff = heights[i+1] - heights[i];
                
                if (heightDiff <= 0)
                    continue;
                else {
                    if (bricks < heightDiff) {
                        i;
                        break;
                    }
                    else bricks -= heightDiff;
                }
            }
            
            return i;
        }
        
        // min heap
        std::priority_queue<int, vector<int>, std::greater<int>> gaps;
        int i = 0;
        
        for (i = 0; i < heights.size() - 1; ++i) {
            if (heights[i+1] <= heights[i])
                continue;
            
            int heightDiff = heights[i+1] - heights[i]; // heightDiff > 0
            
            if (gaps.size() >= ladders && bricks < heightDiff && bricks < gaps.top()) {
                break;
            }
            
            if (gaps.size() < ladders)
                gaps.push(heightDiff);
            else {
                if (bricks >= std::min(gaps.top(), heightDiff)) {
                    if (heightDiff < gaps.top()) {
                        bricks -= heightDiff;
                    }
                    else {
                        bricks -= gaps.top();
                        gaps.pop();
                        gaps.push(heightDiff);
                    }
                }
            }
        }
               
        
        return i;
    }
};