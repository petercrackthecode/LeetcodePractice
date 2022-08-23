// link: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3291/

bool backspaceCompare(string S, string T)
{
    int longestLength = S.length() > T.length() ? S.length() : T.length(),
        traversalIndex{0};

    std::string convertedS{""},
        convertedT{""};

    while (traversalIndex < longestLength)
    {
        if (S.length() > traversalIndex)
        {
            if (S[traversalIndex] != '#')
            {
                convertedS += S[traversalIndex];
            }
            else
            {
                if (convertedS.length() != 0)
                    convertedS.pop_back();
            }
        }

        if (T.length() > traversalIndex)
        {
            if (T[traversalIndex] != '#')
            {
                convertedT += T[traversalIndex];
            }
            else
            {
                if (convertedT.length() != 0)
                    convertedT.pop_back();
            }
        }

        ++traversalIndex;
    }

    return convertedT == convertedS;
}