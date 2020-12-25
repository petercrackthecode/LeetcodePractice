// link: https://leetcode.com/problems/diagonal-traverse/
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        if (matrix.empty())
            return vector<int>();
        
        int M = matrix.size(),
            N = matrix[0].size();
        int row = 0,
            col = 0;
        
        vector<int> ans;
        
        bool isMovingUp = true;
        
        while (ans.size() < M * N) {
            if (isMovingUp) {
                ans.push_back(matrix[row][col]);
                if (row - 1 >= 0 && col + 1 < N) {
                    --row;
                    ++col;
                }
                else {
                    isMovingUp = false;
                    if (col + 1 < N)
                        ++col;
                    else if (row + 1 < M)
                        ++row;
                    else break;
                }
            }
            else { // moving down
                ans.push_back(matrix[row][col]);
                if (col - 1 >= 0 && row + 1 < M) {
                    --col;
                    ++row;
                }
                else {
                    isMovingUp = true;
                    if (row + 1 < M)
                        ++row;
                    else if (col + 1 < N)
                        ++col;
                    else break;
                }
            }
        }
        
        return ans;
    }
};