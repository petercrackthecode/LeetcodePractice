// link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
class Solution {
public:
	string removeDuplicates(string s, int k) {
		bool replaced = true;

		while (replaced) {
			replaced = false;
			int cnt = 1;

			for (int i = 1; i < s.size(); ++i) {
				if (s[i] == s[i-1]) {
					if (++cnt == k)	{
						s = s.substr(0, i - k + 1) + s.substr(i + 1);
						replaced = true;
					}
				}
				else cnt = 1;
			}
		}

		return s;
	}
}