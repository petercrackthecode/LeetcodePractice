class Solution {
public:
    void sortADiagnalRow(vector<vector<int>>& mat, 
                         int m, int n,
                         std::vector<int>& diagnal, 
                         int sr, int sc) {
        int r, c, size;
        
        for (r = sr, c = sc, size = 0; r < m && c < n; r++, c++, size++) {
            diagnal[size] = mat[r][c];
            // std::cout << " " << diagnal[size];
        }
        // std::cout << std::endl;
        // std::cout << "size: " << size << std::endl;
        std::sort(diagnal.begin(), diagnal.begin() + size);
        
        for (r = sr, c = sc, size = 0; r < m && c < n; r++, c++, size++) {
            mat[r][c] = diagnal[size];
            // std::cout << " " << mat[r][c];
        }
        // std::cout << std::endl;

    }
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        
        int diagnal_max = std::min(m, n);
        
        std::vector<int> diagnal(diagnal_max);
        
        int sr, sc;
        for (sr = 0, sc = 0; sc < n-1; sc++) {
            // std::cout << "sr: " << sr << " sc: " << sc << std::endl;
            sortADiagnalRow(mat, m, n, diagnal, sr, sc);
        }
        for (sr = 1, sc = 0; sr < m-1; sr++) {
            // std::cout << "sr: " << sr << " sc: " << sc << std::endl;
            sortADiagnalRow(mat, m, n, diagnal, sr, sc);
        }

        return mat;
    }
};