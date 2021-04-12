// link: https://leetcode.com/submissions/detail/479887774/?from=explore&item_id=3702
class Solution {
public:
	unordered_map<char, char> mp;
	bool isAlienSorted(vector<string> &words, string order) {
		for (int i = 0; i < size(order); ++i)
			mp[order[i]] = i + 'a';
		for (auto &word : words) {
			for (auto &c : word)
				c = mp[c];
		}

		return is_sorted(begin(words), end(words));
	}
}