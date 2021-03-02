// link: https://leetcode.com/problems/set-mismatch/

class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] count = new int[nums.length];
        int[] result = new int[2];
        for (int num : nums) {
            count[num - 1]++;
        }
        for (int i = 0; i < nums.length; i++) {
            if (count[i] == 2) {
                result[0] = i + 1;
            }
            if (count[i] == 0) {
                result[1] = i + 1;
            }
        }
        return result;
    }
}

