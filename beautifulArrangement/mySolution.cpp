// link: https://leetcode.com/problems/beautiful-arrangement/

class Solution {
public:
    
    /* 1. Select a number from 1 to n.
       2. If the number hasn't been selected in the map, and the number matches one of the following condition:
            - perm[i] is divisible by i.
            - i is divisible by perm[i].
          Pick that number, and saved it in the map.
          If the number doesn't match any of the aforementioned conditions, go back to step 1.
       3. If i == 1 and the number is selected, ++count.
       
       Do the step 1 for all the elements in the array from 1 to n.
    
    */
    typedef std::map<int, bool> mib;
    
    auto countArrangementRecursively(int currentPosition, int n, mib selectedNumbers, int &answer) -> void {
        for (int num = n; num > 0; --num) {
            if ((num % currentPosition == 0 || currentPosition % num == 0) && !selectedNumbers[num]) {
                selectedNumbers[num] = true;
                if (currentPosition == 1) {
                    ++answer;
                }
                else countArrangementRecursively(currentPosition - 1, n, selectedNumbers, answer);
                
                selectedNumbers[num] = false;
            }
        }
    }
    
    int countArrangement(int n) {
        int answer = 0;
        
        mib selectedNumbers;
        
        countArrangementRecursively(n, n, selectedNumbers, answer);
        
        
        return answer;
    }
};