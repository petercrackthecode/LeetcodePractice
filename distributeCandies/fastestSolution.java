// https://leetcode.com/problems/distribute-candies/
class Solution {
    public int distributeCandies(int[] candies) {
        int candiesToEat = candies.length / 2;
        int typeCount = 0;
        boolean[] typeUsed = new boolean[200001];
        for (int c: candies) {
            int t = c + 100000;
            if (!typeUsed[t]) {
                if (++typeCount >= candiesToEat)  return candiesToEat;
                typeUsed[t] = true;
            }
        }
        return typeCount;
    }
}