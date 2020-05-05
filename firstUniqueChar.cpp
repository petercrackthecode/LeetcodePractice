// link: https://leetcode.com/problems/first-unique-character-in-a-string/
int firstUniqChar(string s)	{
    std::vector<int> charactersCount(26, 0);

    for (char ch : s)
    {
        ++charactersCount[ch - 'a'];
    }

    for (unsigned int index = 0; index < s.length(); ++index)
    {
        if (charactersCount[s[index] - 'a'] == 1)
            return static_cast<int>(index);
    }

    return -1;
}