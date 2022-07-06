// link: https://leetcode.com/problems/first-bad-version/
int firstBadVersion(int n) {
        int low= 1,
            high= n,
            mid= (high - low) / 2 + low;
        
        while (!(isBadVersion(mid) && !isBadVersion(mid - 1))) {
            if (isBadVersion(mid)) {
                high= mid - 1;
            }
            else {
                low= mid + 1;
            }
            mid= (high - low) / 2 + low;
        }
        
        return mid;
    }