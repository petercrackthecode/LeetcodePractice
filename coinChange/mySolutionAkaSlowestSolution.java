// link: https://leetcode.com/problems/coin-change/

class Solution {
    private HashMap<Integer, Integer> minCoinsNumToReturnN = new HashMap<>();
    
    /*
        1. Iterate through the coins array, take a coin, subtract the amount by that coin's value, call it the new amount.
        2. Pass the new amount to the coinChangeRecursive function. The function will return the minimum amount of coins used to return that new Amount's value.
        3. Among all the time we pass newAmount to coinChangeRecursive, return the smallest amount of coins used.
    */
    
    /*
        The coinChangeRecursive function:
        1. For a certain input amount, see if that amount exist in the HashMap. If yes, return map[amount].
        2. If no, iterate through all the coins in the coins array, see if that coin's value is smaller than the total amount's value. If yes, get the new amount, and pass it to the coinChangeRecursive function.
        3. if none of the coins is smaller (aka subtractable to) than amount, return -1.
    */
    
    private int coinChangeRecursive(int[] coins, int amount) {
        if (!minCoinsNumToReturnN.containsKey(amount)) {
            Integer minWay = Integer.MAX_VALUE,
                    currentWay = Integer.MAX_VALUE;
            int index = 0;
            while (index < coins.length && amount >= coins[index]) {
                currentWay = coinChangeRecursive(coins, amount - coins[index]);
                currentWay = currentWay.equals(Integer.MAX_VALUE) ? Integer.MAX_VALUE : (1 + currentWay);
                minWay = Math.min(minWay, currentWay);
                
                ++index;
            }
            
            minCoinsNumToReturnN.put(amount, minWay);
        }
        
        return minCoinsNumToReturnN.get(amount);
            
    }
    
    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins); // sort ascendingly
        minCoinsNumToReturnN.put(0, 0);
        int ans = coinChangeRecursive(coins, amount);
        return (ans == Integer.MAX_VALUE ? -1 : ans);
    }
}