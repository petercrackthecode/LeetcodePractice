class Solution {
private:
    vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};
public:
    /* 
        1. Iterate through the indices of the string.
        2. Pick a vowel, see if that character is lexicographically greater than the last character in the substring:
            - Yes, make that character the last added character. Move on to the next index in the substring.
            - No, skip the current vowel, move on to the next vowel.
        3. If this index == n-1 and the string is valid, increment the answer by one, else keep looping.
    */
    auto countVowelStringsRecursive(int remainingCharactersInSubstrCount, char lastVowel, int &ans) -> void {
        for (int index = 0; index < vowels.size(); ++index) {
            if (vowels[index] >= lastVowel) {
                if (remainingCharactersInSubstrCount - 1 <= 0) {
                    ++ans;
                }
                else countVowelStringsRecursive(remainingCharactersInSubstrCount - 1, vowels[index], ans);
            }
        }
    }
    
    int countVowelStrings(int n) {
        int ans = 0;
        countVowelStringsRecursive(n, 'a', ans);
        return ans;
    }
};