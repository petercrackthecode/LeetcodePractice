// link: https://leetcode.com/problems/word-subsets/
class Solution {
private:
    void setup_frequency(std::map<char, int> &b_words_frequency, const std::map<char, int> &current_word_frequency) {
        for (auto const& character_frequency : current_word_frequency) {
           b_words_frequency[character_frequency.first] = std::max(b_words_frequency[character_frequency.first], character_frequency.second);
        }
    }
    
    bool is_word_universal(std::map<char, int> word_in_A_frequency, std::map<char, int> b_words_frequency) {
        for (auto const& ele : b_words_frequency) {
            if (ele.second > word_in_A_frequency[ele.first])
                return false;
        }
        
        return true;
    }
    
public:
    vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
        std::map<char, int> b_words_frequency;
        vector<string> ans;
        
        for (auto word : B) {
            map<char, int> current_word_frequency;
            for (auto ch : word) {
                ++current_word_frequency[ch];
            }
            
            setup_frequency(b_words_frequency, current_word_frequency);
        }
        
        for (auto word : A) {
            map<char, int> current_word_frequency;
            for (auto ch : word) {
                ++current_word_frequency[ch];
            }
            
            if (is_word_universal(current_word_frequency, b_words_frequency))
                ans.push_back(word);
        }
        
        return ans;
    }
};