class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int missingNum{0};
        int index = 0;
        while (k != 0) {
            ++missingNum;
            if (missingNum != arr[index]) {
                --k;
            }
            else if (index < arr.size() - 1)
                ++index;
        }
            
        return missingNum;
    }
};