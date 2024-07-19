# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        - all the versions after a bad version are also bad.
         0  1       n-1
        [1, 2, ..., n]

        - binary search
        - left = 0
        - right = n - 1

        n = 5, bad = 4

         0  1  2  3  4
        [1, 2, 3, 4, 5]
                  l
                     r
               m

        - if isBadVersion(m) is True and (m equals 0 or the previous version (m-1) is not bad (isBadVersion(m-1) == False)):
            - return m+1
        - if isBadVersion(m) is False => the first bad version must be after index m => move right:
            - l = m + 1
        - otherwise: m is a bad version, but not the first bad version => move left:
            - r = m - 1

        - return n+1
        """
        left, right = 1, n

        while left <= right:
            mid: int = left + (right - left) // 2
            if isBadVersion(mid) and (mid == 0 or not isBadVersion(mid - 1)):
                return mid
            elif not isBadVersion(mid):  # move right
                left = mid + 1
            else:  # move left
                right = mid - 1
        # no version is bad from 1..n, return a dummy value
        return n + 1
