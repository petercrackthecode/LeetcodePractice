// link: https://leetcode.com/problems/power-of-three/
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n<=0) return false;        
        // int mxThreshold = 0x7FFFFFFF/3;
        // int mxPoTr = 3;
        // while(mxPoTr < mxThreshold){
        //     mxPoTr = mxPoTr*3;
        // }
        // std::cout << mxPoTr << std::endl;
        int mxPoTr = 1162261467;
        return (mxPoTr%n == 0) ;
    }
};