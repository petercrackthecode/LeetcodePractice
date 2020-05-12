// link: https://leetcode.com/problems/single-element-in-a-sorted-array/
bool checkDuplicate(std::vector<int> nums, int position)    {
    bool hasLeftBound = position - 1 >= 0,
         hasRightBound = position + 1 <= nums.size() - 1;
    if (hasLeftBound && hasRightBound)  {
        return !(nums[position] == nums[position - 1] || nums[position] == nums[position + 1]);
    }
    else if (hasLeftBound)  {
        return !(nums[position] == nums[position - 1]);
    }
    else    {
        return !(nums[position] == nums[position + 1]);
    }
}

int singleNonDuplicate(vector<int> &nums)   {
    int left = 0,
        right = nums.size() - 1,
        mid = (right - left) / 2 + left;

    while (left <= right)   {
        if (checkDuplicate(nums, mid))
            return nums[mid];
        else    {
            if (mid % 2 == 0)   {
                right = mid - 1;
            }
            else    {
                left = mid + 1;
            }
            mid = (right - left) / 2 + left;
        }
    }

    return 0;
}