using System.Collections.Generic;

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> numIndex = new Dictionary<int, int>();
        
        for (int index = 0; index < nums.Length; ++index) {
            var currentNum = nums[index];
            numIndex[currentNum] = index;
        }

        for (int index = 0; index < nums.Length; ++index) {
            int currentNum = nums[index],
                remainder = target - currentNum;
            
            if (numIndex.ContainsKey(remainder)) {
                if (currentNum == remainder && index == numIndex[remainder]) {
                    continue;
                }
                
                return new int[]{index, numIndex[remainder]};
            }
        }

        return new int[]{0, 0};
    }
}