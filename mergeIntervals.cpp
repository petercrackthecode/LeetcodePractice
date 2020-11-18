// link: https://leetcode.com/problems/merge-intervals/
vector<vector<int>> merge(vector<vector<int>>& in){
        vector<pair<int,int>> intervals;
        int n = in.size();
        
        for (int i=0;i<n;i++)
            intervals.push_back(make_pair(in[i][0],in[i][1]));
        
        sort(intervals.begin(),intervals.end());  
        
        vector<vector<int>> ans;
        int start = intervals[0].first, end = intervals[0].second;
        
        for (int i=1;i<n;i++){
            if (end >= intervals[i].first){
                end = max(end, intervals[i].second);
            } else {
                ans.push_back({start,end});
                start = intervals[i].first; end = intervals[i].second;
            }
        }
        
        ans.push_back({start,end});
        return ans;
    }