// link: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
class Solution {
public:
    static int combinationOfTwo(int objectsNum) {
        if (objectsNum < 2)
            return 0;
        
        int ans = 0;
        
        int addedCombination = objectsNum - 1;
        while (addedCombination > 0) {
            ans += addedCombination;
            --addedCombination;
        }
        
        return ans;
    }
    
    int numPairsDivisibleBy60(vector<int>& time) {
        if (time.size() <= 1)
            return 0;
        
        int ans{0};
        
        int min = INT_MAX,
            secondToMin = INT_MAX;
        
        int max = INT_MIN,
            secondToMax = INT_MIN;
        
        map<int, int> timeFrequencies;
        
        for (auto songTime : time) {
            ++timeFrequencies[songTime];
            
            if (songTime > min) {
                secondToMin = std::min(secondToMin, songTime);
            }
            else { // songTime <= min, found a new min
                secondToMin = min;
                min = std::min(songTime, min);
            }
            
            if (songTime < max) {
                secondToMax = std::max(secondToMax, songTime);
            }
            else { // songTime >= max, found a new max
                secondToMax = max;
                max = std::max(songTime, max);
            }
        }
        
        int startFrom = ceil((min + secondToMin) / 60.0) * 60, // round up, use ceil
            endTo = floor((max + secondToMax) / 60.0) * 60; // round down, use floor
        
        int currentTime = 0,
            currentFreq = 0,
            remainder = 0;
        
        for (auto freq : timeFrequencies) {
            currentTime = freq.first;
            currentFreq = freq.second;
            
            for (int sum = startFrom; sum <= endTo; sum += 60) {
                remainder = sum - currentTime;
                if (remainder >= currentTime && timeFrequencies.count(remainder) > 0) {
                    if (remainder == currentTime)
                        ans += combinationOfTwo(currentFreq);
                    else ans += currentFreq * timeFrequencies[remainder];
                }
            }
        }
        
        return ans;
    }
};