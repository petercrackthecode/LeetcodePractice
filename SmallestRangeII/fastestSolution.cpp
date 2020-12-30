class Solution {
public:
    int smallestRangeII(vector<int>& A, int K) {
        sort(A.begin(), A.end());
        
        int mi = *A.begin();
        int ma = *A.rbegin();
        int ans = ma - mi;
        
        for (int i = 0; i < A.size() - 1; ++i){
            int a = A[i];
            int b = A[i + 1];
            
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K));
        }
            
        return ans;
    }
};