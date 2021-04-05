// link: https://leetcode.com/problems/global-and-local-inversions
class Solution {
    private int binarySearch(ArrayList<Integer> arr, int target) {
        int left = 0,
            right = arr.size() - 1;
        int foundPos = -1;
        
        while (left <= right && foundPos == -1) {
            int mid = left + (right - left)/2;
            if (arr.get(mid) == target)
                foundPos = mid;
            else if (arr.get(mid) < target) {
                left = mid + 1;
            }
            else right = mid - 1;
        }
        
        return foundPos;
    }
    
    public boolean isIdealPermutation(int[] A) {
        int localInversion = 0,
            globalInversion = 0;
        // int trackIndex[] = new int[A.length];
        
        ArrayList<Integer> arr = new ArrayList();
        
        for (int index = 0; index < A.length; ++index) {
            if (index < A.length - 1 && A[index] > A[index + 1])
                ++localInversion;
            // trackIndex[A[index]] = index;
            
            arr.add(index);
        }
        
        for (int index = 0; index < A.length; ++index) {
            int foundIndex = binarySearch(arr, A[index]);
            if (foundIndex == -1)
                continue;
            globalInversion += foundIndex;
            if (!arr.isEmpty())
                arr.remove(foundIndex);
        }
        
        return localInversion == globalInversion;
    }
}