// leetcode: https://leetcode.com/problems/rotate-image/
class Solution {
public:
    static void swap(int &a, int &b) {
        int temp = a;
        a = b;
        b = temp;
    }
    
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int top = 0,
            bottom = n - 1,
            left = 0,
            right = n - 1;
        
        pair<int, int> rightToLeft,
                       topToBottom,
                       leftToRight,
                       bottomToTop;
        
        while (left < right && top < bottom) {
            rightToLeft = make_pair(top, right);
            topToBottom = make_pair(top, left);
            leftToRight = make_pair(bottom, left);
            bottomToTop = make_pair(bottom, right);
            
            while (rightToLeft.second > left && topToBottom.first < bottom && leftToRight.second < right && bottomToTop.first > top) {
                swap(matrix[rightToLeft.first][rightToLeft.second], matrix[topToBottom.first][topToBottom.second]);
                swap(matrix[topToBottom.first][topToBottom.second], matrix[leftToRight.first][leftToRight.second]);
                swap(matrix[leftToRight.first][leftToRight.second], matrix[bottomToTop.first][bottomToTop.second]);
                
                --rightToLeft.second;
                ++topToBottom.first;
                ++leftToRight.second;
                --bottomToTop.first;
            }
            
            ++top;
            --bottom;
            ++left;
            --right;
        }
    }
};