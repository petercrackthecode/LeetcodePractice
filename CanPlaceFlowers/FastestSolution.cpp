// link: https://leetcode.com/problems/can-place-flowers/
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (n == 0) return true;
        int count = 0;
        for (int i = 0; i < flowerbed.size(); i++){
            if (flowerbed[i] == 0){
                bool front = (i == 0 || flowerbed[i - 1] == 0);
                bool behind = (i == flowerbed.size() - 1 || flowerbed[i + 1] == 0);
                if (front && behind){
                    flowerbed[i] = 1;
                    count++;
                    if (count >= n)
                        return true;
                }
            }
        }
        return false;
    }
};