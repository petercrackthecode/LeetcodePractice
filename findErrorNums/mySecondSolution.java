// link: https://leetcode.com/problems/set-mismatch/

class Solution {
    public int[] findErrorNums(int[] nums) {
        Arrays.sort(nums);
        
        int extraNum = Integer.MAX_VALUE,
            missedNum = Integer.MIN_VALUE;
        
        for (int index = 0; index < nums.length; ++index) {
            if (index == 0) {
                if (nums[index] != 1)
                    missedNum = 1;
            }
            else {
                if (nums[index] == nums[index - 1])
                    extraNum = nums[index];
                else if (nums[index] - nums[index - 1] > 1)
                    missedNum = nums[index] - 1;
            }
        }
        
        if (nums[nums.length - 1] < nums.length)
            missedNum = nums.length;
        
        int ans[] = {extraNum, missedNum};
        
        return ans;
    }
}