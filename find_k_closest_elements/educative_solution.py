# https://leetcode.com/problems/find-k-closest-elements/
def binary_search(array, target):

    # initialize the left and the right pointer
    left = 0
    right = len(array) - 1

    # find the first closest element to target while left is less than or equal to right
    while left <= right:

        # compute the middle index
        mid = (left + right) // 2

        # if the value at mid is equal to target, return mid
        if array[mid] == target:
            return mid

        # if the value at mid is less than target, move left forward
        if array[mid] < target:
            left = mid + 1

        # if the value at mid is greater than target, move right backward
        else:
            right = mid - 1
    return left


def find_closest_elements(nums, k, target):
    if len(nums) == k:
        return nums

    if target <= nums[0]:
        return nums[0:k]

    if target >= nums[-1]:
        return nums[len(nums) - k : len(nums)]

    first_closest = binary_search(nums, target)

    window_left = first_closest - 1
    window_right = window_left + 1

    while (window_right - window_left - 1) < k:
        if window_left == -1:
            window_right += 1
            continue

        if window_right == len(nums) or abs(nums[window_left] - target) <= abs(
            nums[window_right] - target
        ):
            window_left -= 1

        else:
            window_right += 1

    return nums[window_left + 1 : window_right]
