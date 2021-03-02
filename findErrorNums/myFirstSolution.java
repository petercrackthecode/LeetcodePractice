// link: https://leetcode.com/problems/set-mismatch/

class Solution {
    public int[] findErrorNums(int[] nums) {
        int extraNum = 0, missedNum = 0;
        
        HashMap<Integer, Boolean> hasNumberAppeared = new HashMap<Integer, Boolean>();
        
        for (int index = 1; index <= nums.length; ++index) {
            hasNumberAppeared.put(index, false);
        }
        
        for (int index = 0; index < nums.length; ++index) {
            if (hasNumberAppeared.get(nums[index]))
                extraNum = nums[index];
            else hasNumberAppeared.put(nums[index], true);
        }
        
        for (Map.Entry<Integer, Boolean> entry : hasNumberAppeared.entrySet()) {
            if (!entry.getValue()) {
                missedNum = entry.getKey();
                break;
            }
        }
        
        int ans[] = new int[]{extraNum, missedNum};
        
        return ans;
    }
}