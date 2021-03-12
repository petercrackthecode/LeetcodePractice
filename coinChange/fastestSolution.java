// link: https://leetcode.com/problems/coin-change/

class Solution {
    public int coinChange(int[] coins, int amount) {
        //1 + min(10,6,9);
        
     Arrays.sort(coins);
        int[] min = new int[]{Integer.MAX_VALUE};
        dfs(coins, coins.length - 1, amount, 0, min);
        return (min[0] == Integer.MAX_VALUE) ? -1 : min[0];
    }
    
    private void dfs(int[] coins, int index, int amount, int count, int[] min) {
        if (amount < 0) {
            return;
        }

        for (int num = amount / coins[index]; num >= 0; num--) {
            int remain = amount - num * coins[index];
            if (remain == 0) {
                min[0] = Math.min(min[0], num + count);
            }

            if (count + num + 1 < min[0] && index > 0) {
                dfs(coins, index - 1, remain, count + num, min);
            } else {
                return;
            }
        }
    }
}