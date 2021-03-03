// link: https://leetcode.com/problems/missing-number/

class Solution {
    public int missingNumber(int[] nums) {
        long sum = 0;
        for (int num = 1; num <= nums.length; ++num) {
            sum += num;
        }
        
        for (int num : nums)
            sum -= num;
        
        return (int)sum;
    }
}