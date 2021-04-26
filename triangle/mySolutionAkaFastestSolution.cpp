// link: https://leetcode.com/problems/triangle/
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int height = triangle.size();
        
        for (int index = height - 1; index > 0; --index) {
            int cols = triangle[index].size();
            
            for (int i = 0; i < cols - 1; ++i) {
                triangle[index - 1][i] = triangle[index - 1][i] + std::min(triangle[index][i], triangle[index][i+1]);
            }
        }
        
        return triangle[0][0];
    }
};