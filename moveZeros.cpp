// link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/

void moveZeroes(std::vector<int> &nums) {
    int noneZerosCounter{0};
    for (int traversalIndex = 0; traversalIndex < nums.size(); ++traversalIndex)
    {
        if (nums[traversalIndex] != 0)
        {
            nums[noneZerosCounter] = nums[traversalIndex];
            ++noneZerosCounter;
        }
    }

    while (noneZerosCounter < nums.size())
    {
        nums[noneZerosCounter] = 0;
        ++noneZerosCounter;
    }
}

// Note:
// 1. You must do this in-place without making a copy of the array.
// 2. Minimize the total number of operations.