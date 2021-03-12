// link: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution {
    public boolean hasAllCodes(String s, int k) {
        if (s.length() < (1 << k) + k - 1) {
            return false;
        }
        int n = 0;
        char[] chars = s.toCharArray();
        for (int i = 0; i < k - 1; i++) {
            n = (n << 1) + (chars[i] - '0');
        }
        int size = 1 << k;
        int mask = size - 1;
        boolean[] exists = new boolean[size];
        for (int i = k - 1; i < chars.length; i++) {
            n = ((n << 1) + chars[i] - '0') & mask;
            if (!exists[n]) {
                exists[n] = true;
                if (--size == 0) {
                    return true;
                }
            }
        }
        return false;
    }
}