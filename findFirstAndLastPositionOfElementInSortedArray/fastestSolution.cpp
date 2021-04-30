// link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution {
public:
    
    int bs(const vector<int>& nums, int target){
        int lo = 0;
        int hi = nums.size();
        while(hi>lo){
            int mid = (lo+hi)/2;
            if (nums[mid] > target){
                hi = mid;
            }else if(nums[mid] < target){
                lo = mid+1;
            }else{
                return mid;
            }
        }
        return -1;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        int index = bs(nums,target);
        if (index == -1){
            return vector<int>{-1,-1};
        }
        
        int lo = 0;
        int hi = index;
        
        while(lo<hi){
            int mid = (lo+hi)/2;
            if (nums[mid] <target){
                lo = mid+1;
            }else{
                hi = mid;
            }
        }
        int res = lo;
        
        lo = index;
        hi = nums.size();
        while(lo<hi){
            int mid = (lo+hi)/2;
            if(nums[mid] > target){
                hi = mid;
            }else{
                lo = mid+1;
            }
        }
        
        return vector<int>{res,lo-1};
            
        
            
    }
};