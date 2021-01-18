// link: https://leetcode.com/problems/max-number-of-k-sum-pairs/
typedef std::map<int, std::list<int>> mili;

class Solution {
public:
    /*
        We'll use a map of <int, list<int>> to save values. int will be the value of the element whereas list<int> will contain the indices that have the element's value in the array order (left -> right).
        1. Traverse through the array, populate the map.
        2. Traverse through the array the second time, for an element A:
           - See if map[A] has a value && map[A] == the index of A: the first element with value A is staying at the current index.
           - See if (k - A) exist in the map, if k - A == A, see if map[k-A].size() > 1, if both conditions match, remove the first index in the list map[A] and map[k - A], increment answer by 1.
    */
    
    int maxOperations(vector<int>& nums, int k) {
        mili indicesWithThatValue;
          
        int ans = 0,
            currentNum = 0,
            remainingK = 0;
        
        for (int index = 0; index < nums.size(); ++index) {
            indicesWithThatValue[nums[index]].push_back(index);
        }
        
        for (int index = 0; index < nums.size(); ++index) {
            currentNum = nums[index];
            remainingK = k - nums[index];
            
            if (indicesWithThatValue.count(currentNum) > 0 && !indicesWithThatValue[currentNum].empty()) {
                indicesWithThatValue[currentNum].pop_front();
                
                if (remainingK == currentNum) {
                    if (!indicesWithThatValue[currentNum].empty()) {
                        ++ans;
                        indicesWithThatValue[currentNum].pop_front();
                    }
                }
                else if (indicesWithThatValue.count(remainingK) > 0 && !indicesWithThatValue[remainingK].empty()) {
                   ++ans;
                   indicesWithThatValue[remainingK].pop_front();
                }
            }
        }
        
        return ans;
    }
};