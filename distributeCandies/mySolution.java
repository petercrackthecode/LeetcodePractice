// https://leetcode.com/problems/distribute-candies/
class Solution {
    public int distributeCandies(int[] candies) {
        HashMap<Integer, Integer> candiesType = new HashMap<Integer, Integer>();
        for (int candy : candies) {
            if (candiesType.containsKey(candy)) {
                candiesType.put(candy, candiesType.get(candy) + 1);
            }
            else {
                candiesType.put(candy, 1);
            }
        }
        
        return Math.min(candiesType.size(), candies.length / 2);
    }
}