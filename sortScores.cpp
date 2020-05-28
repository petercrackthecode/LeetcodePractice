// link: https://www.interviewcake.com/question/cpp/top-scores?course=fc1&section=hashing-and-hash-tables
vector<int> sortScores(const vector<int>& unorderedScores, int highestPossibleScore)
{
    // sort the scores in O(n) time
    std::vector<int> scoresCount(highestPossibleScore + 1, 0),
                     sortedScores;
    
    for (auto elem : unorderedScores) {
        ++scoresCount[elem];
    }
    
    for (int score= scoresCount.size(); score > 0; --score) {
        while (scoresCount[score] > 0) {
            sortedScores.push_back(score);
            --scoresCount[score];
        }
    }
    
    
    return sortedScores;
}
