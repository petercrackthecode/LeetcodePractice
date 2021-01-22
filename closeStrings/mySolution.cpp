class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.length() != word2.length())
            return false;
        
        map<char, int> word1FrequenciesTracker,
                       word2FrequenciesTracker;
        
        vector<int> word1CharactersFrequencies,
                    word2CharactersFrequencies;
        
        for (int index = 0; index < word1.length(); ++index) {
            ++word1FrequenciesTracker[word1[index]];
        }
        
        // save all the values in frequenciesTracker into an array;
        
        
        for (auto pair : word1FrequenciesTracker) {
            word1CharactersFrequencies.push_back(pair.second);
        }
        
        
        for (int index = 0; index < word2.length(); ++index) {
            ++word2FrequenciesTracker[word2[index]];
        }
        
        for (auto pair : word2FrequenciesTracker) {
            word2CharactersFrequencies.push_back(pair.second);
            if (word1FrequenciesTracker.count(pair.first) == 0)
                return false;
        }
        
        for (auto pair : word1FrequenciesTracker) {
            if (word2FrequenciesTracker.count(pair.first) == 0)
                return false;
        }
        
        std::sort(word1CharactersFrequencies.begin(), word1CharactersFrequencies.end());
        
        std::sort(word2CharactersFrequencies.begin(), word2CharactersFrequencies.end());
        
        return word1CharactersFrequencies == word2CharactersFrequencies;
    }
};