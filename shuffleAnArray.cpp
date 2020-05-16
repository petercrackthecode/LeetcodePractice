// link: https://leetcode.com/problems/shuffle-an-array/
#include <math.h>
#include <vector>
#include <time.h>

void swap(int &first, int &second) {
    int temp= first;
    first= second;
    second= temp;
}

class Solution {
private:
    std::vector<int> shuffled, 
                     original;
public:    
    Solution(vector<int>& nums) {
        shuffled= nums;
        original = nums;
        srand(time(NULL));
    }
     
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        shuffled= original;
        return original;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        int size= shuffled.size();
        int i= 0;
        while (size > 0) {
            int randomIndex= rand() % size + i;
            swap(shuffled[randomIndex], shuffled[shuffled.size() - size]);
            --size;
            ++i
        }

        return shuffled;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */