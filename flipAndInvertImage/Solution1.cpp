class Solution {
public:
    static void swap(int &a, int &b) {
        int temp = b;
        b = a;
        a = temp;
    }
    
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int n = A.size();
        
        int i = 0, 
            j = 0;
        
        while (i < n) {
            j = 0;
            while (j < n/2) {
                swap(A[i][j], A[i][n - j - 1]);
                A[i][j] = (A[i][j] == 0) ? 1 : 0;
                A[i][n-j-1] = (A[i][n-j-1] == 0) ? 1 : 0;
                ++j;
            }
            
            if (n % 2 != 0) {
                A[i][n/2] = (A[i][n/2] == 0) ? 1 : 0;
            }
            
            ++i;
        }
        
        return A;
    }
};