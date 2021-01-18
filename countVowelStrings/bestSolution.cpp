class Solution {
public:
    int countVowelStrings(int n) {
     
       vector<int> combi = {1,1,1,1,1};
    
        for(int i = 2; i<=n; i++){
            combi[4] = combi[0] + combi[1] + combi[2] + combi[3] + combi[4];
            combi[3] = combi[0] + combi[1] + combi[2] + combi[3];
            combi[2] = combi[0] + combi[1] + combi[2];
            combi[1] = combi[0] + combi[1];
            combi[0] = combi[0];
        }
                
        return combi[0] + combi[1] + combi[2] + combi[3] + combi[4];
    }
};