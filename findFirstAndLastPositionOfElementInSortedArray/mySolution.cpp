// link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#include <vector>
using namespace std;

class Solution
{
private:
    int start, end;
    auto searchRangeHelper(const vector<int> &nums, const int &target, const int &left, const int &right) -> void
    {
        if (left <= right)
        {
            int mid = (right - left) / 2 + left;
            if (nums[mid] == target)
            {
                start = std::min(start, mid);
                end = std::max(end, mid);

                if (mid - 1 >= left && nums[mid - 1] == target && mid - 1 < start)
                    searchRangeHelper(nums, target, left, mid - 1);
                if (mid + 1 <= right && nums[mid + 1] == target && mid + 1 > end)
                    searchRangeHelper(nums, target, mid + 1, right);
            }
            else if (nums[mid] < target)
            {
                searchRangeHelper(nums, target, mid + 1, right);
            }
            else
            { // nums[mid] > target
                searchRangeHelper(nums, target, left, mid - 1);
            }
        }
    }

public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        if (nums.size() == 0)
            return {-1, -1};

        start = nums.size(), end = -1;

        int left = 0,
            right = nums.size() - 1;
        searchRangeHelper(nums, target, left, right);

        if (start == nums.size() || end == -1)
            return {-1, -1};
        else
            return {start, end};
    }
};