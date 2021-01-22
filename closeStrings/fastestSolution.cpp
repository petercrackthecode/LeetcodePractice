class Solution {
     static constexpr int ALPHABET = 26;

public:
    static auto closeStrings(std::string_view w1, std::string_view w2) -> bool
    {
        std::ios::sync_with_stdio(false);
        std::cin.tie(nullptr);

        if (w1.size() != w2.size()) {
            return false;
        }
        std::array<int, ALPHABET> cnt1 {};
        std::array<int, ALPHABET> cnt2 {};
        for (char ch : w1) {
            cnt1[ch - 'a']++;
        }
        for (char ch : w2) {
            cnt2[ch - 'a']++;
        }
        if (!equal(begin(cnt1), end(cnt1), begin(cnt2), end(cnt2), [](int a, int b) { return bool (a) == bool (b); })) {
            return false;
        }
        sort(begin(cnt1), end(cnt1));
        sort(begin(cnt2), end(cnt2));
        return cnt1 == cnt2;
    }
};