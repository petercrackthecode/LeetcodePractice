// link: https://leetcode.com/problems/smallest-integer-divisible-by-k/
class Solution {
public:
    int smallestRepunitDivByK(int K) {
        if (K % 2 == 0 || K % 5 == 0)
            return -1;
        if (K == 1)
            return 1;
        unsigned int sumOfRemainders = 1;
        int currentRemainder = 1,
            // lastRemainder = -1,
            digitsCount = 1;
        
        while (currentRemainder != 0 && (sumOfRemainders % K != 0)) {
            currentRemainder = (currentRemainder * 10) % K;
            sumOfRemainders += currentRemainder;
            ++digitsCount;
        }
        
        if (sumOfRemainders % K != 0)
            return -1;
        
        return digitsCount;
    }
};