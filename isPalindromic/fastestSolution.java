// https://leetcode.com/problems/longest-palindromic-substring/

class Solution {
	int start = 0, end = 0;

	public String longestPalindrome(String s) {
		if (s.length() < 2)
			return s;
		char[] c = s.toCharArray(); // toCharArray makes it easier to process string
		longestPalindomeAt(c, 0);
		return s.substring(start, end + 1);
	}

	private void longestPalindromeAt(char[] c, int p) {
		int a = p;
		int b = p;
		int n = c.length;

		if (p == n - 1 || (n - p) < (end - start + 1)/2) {
			return;
		}

		while (b < n-1 && c[b] == c[b+1]) {
			++b;
		}

		p = b;

		while (a > 0 && b < n-1 && c[a-1] == c[b+1]) {
			--a;
			++b;
		}

		if (b - a > end - start) {
			end = b;
			start = a;
		}

		longestPalindromeAt(c, p + 1);
	}
}