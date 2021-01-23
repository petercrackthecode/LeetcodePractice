class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int currentRow = mat.size() - 1, 
            currentCol = 0;
        
        int row = currentRow,
            col = currentCol,
            currentIndexInSortedVector;
        
        vector<int> sortedDiagonalLine;
        
        bool isTopLeftSorted = false;
        
        while (!(currentRow == 0 && currentCol == mat[0].size() - 1)) {
            row = currentRow;
            col = currentCol;
                
            while (row < mat.size() && col < mat[0].size()) {
                sortedDiagonalLine.push_back(mat[row][col]);
                ++row;
                ++col;
            }
            
            std::sort(sortedDiagonalLine.begin(), sortedDiagonalLine.end());
            row = currentRow;
            col = currentCol;
            currentIndexInSortedVector = 0;
                
            while (row < mat.size() && col < mat[0].size() && currentIndexInSortedVector < sortedDiagonalLine.size()) {
                mat[row][col] = sortedDiagonalLine[currentIndexInSortedVector];
                ++row;
                ++col;
                ++currentIndexInSortedVector;
            }
            
            sortedDiagonalLine.clear();
            
            if (currentRow >= 0 && !isTopLeftSorted) {
               if (currentRow == 0) {
                   isTopLeftSorted = true;
                   ++currentCol;
               }
               else {
                   --currentRow;
               }
            }
            else if (currentCol < mat[0].size()) {
                ++currentCol;
            }
        }
        
        return mat;
    }
};