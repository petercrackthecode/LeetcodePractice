// https://leetcode.com/problems/repeated-substring-pattern/



// 0459-repeated-substring-pattern
// Q: https://leetcode.com/problems/repeated-substring-pattern/

class Solution {
    
    /* Steps:           "a b c a b c a b c a b c"
                        [0 0 0 1 2 3 1 2 3 1 2 3]
                        "a a c a a c a a c a a c"
                        [0 1 0 1 2 3 1 2 3 1 2 3]
    
    */
    // "a a"
    //  0 1
    // "a b a c"
    //  0 0 1 0
    // "a b a b"
    //  0 0 1 2
    // "a a a a"
    //  0 1 2 3
    // "a b c a b c a b c a b c"
    //  0 0 0 1 2 3 4 5 6 7 8 9
    // P1-210205: KMP
    // Time: O(N)
    // Space: O(N)
    // Rank: 98.16%
    public boolean repeatedSubstringPattern1(String s) {
        int n = s.length();
        int[] lps = new int[n];
        for (int i = 0, j = 1; j < n; ) {
            if (s.charAt(i) == s.charAt(j)) {
                lps[j++] = ++i;
            } else if (i > 0) {
                i = lps[i - 1];
            } else {
                j ++;
            }
        }
        int m = lps[n - 1];
        return m > 0 && m % (n - m) == 0;
    }
    
    public boolean repeatedSubstringPattern2F(String s) {
        int n = s.length();
        int[] lps = new int[n];
        for (int i = 0, j = 1; j < n; ) {
            if (s.charAt(i) == s.charAt(j)) {
                lps[j++] = ++i;
            } else if (i > 0) {
                i = lps[i - 1];
            } else {
                j ++;
            }
        }
        System.out.println(Arrays.toString(lps));
        if (lps[n - 1] == 0) {
            return false;
        }
        int i = n - 2;
        for ( ; i >= 0 && lps[i] + 1 == lps[i + 1] && lps[i] != 0; i --) {
        }
        return lps[n - 1] % (i + 1) == 0;
    }    
    
    // "a b c a b c a b c a b c"
    //  0 0 0 1 2 3 4
    public boolean repeatedSubstringPattern1F(String s) {
        int n = s.length();
        int[] lps = new int[n];
        for (int i = 0, j = 1; j < n; ) {
            if (s.charAt(i) == s.charAt(j)) {
                lps[j++] = ++i;
            } else if (i > 0) {
                i = lps[i - 1];
            } else {
                j ++;
            }
        }
        System.out.println(Arrays.toString(lps));
        int m = lps[n - 1];
        if (m == 0 || n % m != 0) {
            return false;
        }
        for (int i = m; i < n; i ++) {
            if (lps[i] != i % m + 1) {
                return false;
            }
        }        
        return true;
    }    
    
    // Rank: 100%
    // Time: O(N^2 / LogN)
    static int [] primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 };
	public boolean repeatedSubstringPattern(String s) {
		final int n = s.length(), np = primes.length;
		for (int i = 0; i < np && primes[i] <= n; i ++) {
            if (n % primes[i] == 0) {
                int m = n / primes[i];
                String base = s.substring(0, m);
                for (int j = m; j < n && s.substring(j, j + m).equals(base); j += m){
                    if (j + m == n) {
                        return true;
                    }
                }                
            }
		}
		return false;
	}    
}












