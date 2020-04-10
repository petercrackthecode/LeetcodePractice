// link: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/
vector<vector<string>> groupAnagrams(vector<string> &strs)
{
    std::map<string, vector<string>> anagramsMap;
    std::vector<vector<string>> anagramsArray;

    for (string s : strs)
    {
        string temp = s;
        std::sort(temp.begin(), temp.end());
        anagramsMap[temp].push_back(s);
    }

    for (auto anAnagrams : anagramsMap)
    {
        anagramsArray.push_back(anAnagrams.second);
    }

    return anagramsArray;
}