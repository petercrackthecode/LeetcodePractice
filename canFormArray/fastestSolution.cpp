class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        
        map<int, int> indexOf;
        
        int n = arr.size();
        vector<bool> v(n, false);
        
        
        for(int i = 0; i < n; i ++) 
            indexOf[arr[i]] = i;
        
        for(auto vec : pieces) {
            
            if(vec.size() != 0) {
                
                int s = indexOf[vec[0]];
                
                int vs = vec.size();
                for(int i = 0; i < vs; i ++) {
                    if(vec[i] != arr[s + i] || v[s + i])
                        return false;
                    v[s + i] = true;
                    // cout << arr[s + i] << endl;
                }
            }
        }
        
        for(auto x : v)
            if(!x)
                return false;
        return true;
    }
};