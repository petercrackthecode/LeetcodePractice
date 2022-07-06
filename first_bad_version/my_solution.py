# Link: https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """"
        Apply binary search to the array from 1 to n.
        Initialization: left = 1, right = n.
        Every time we do so, have a middle position. Let's call it mid.
        Keep doing binary search until left > right.
        Determine to move to the left side or to the right side of the array every time we have a new
        mid point:
          if isBadVersion(mid) == False: move right
          else: the current mid version is bad => first_bad_version = min(first_bad_version, mid) and move left
        """
        first_bad_version = n
        left, right = [1, n]
        while left <= right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                first_bad_version = min(first_bad_version, mid)
                right = mid - 1

        return first_bad_version
