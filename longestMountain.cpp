#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    void checkLongestLength(int &maxLength, int &leftBound, int &rightBound) {
        if (leftBound == -1 || rightBound == -1) {
            leftBound = -1;
            rightBound = -1;
            return;
        }
        
        maxLength = max(maxLength, rightBound - leftBound + 1);
        
        leftBound = rightBound;
        rightBound = -1;
    }
    
    int longestMountain(vector<int>& A) {
        if (A.size() < 3)
            return 0;
        
        int maxLength = 0;
        
        int leftBound = -1, 
            rightBound = -1;
        
        for (int index = 1; index < A.size(); ++index) {
            if (A[index] == A[index - 1]) {
                checkLongestLength(maxLength, leftBound, rightBound);
                leftBound = rightBound = -1;
            }
            else if (A[index] > A[index - 1]) {
                if (leftBound == -1) {
                    leftBound = index-1;
                }
                else if (rightBound != -1) {
                    checkLongestLength(maxLength, leftBound, rightBound);
                }
            }
            else { // A[index] < A[index - 1]
                if (leftBound != -1) {
                    if (rightBound != -1)
                        ++rightBound;
                    else rightBound = index;
                    
                    if (rightBound >= A.size() - 1)
                        checkLongestLength(maxLength, leftBound, rightBound);
                }
            }
        }
        
        return maxLength;
    }
};