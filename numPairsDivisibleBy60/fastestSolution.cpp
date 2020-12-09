// link: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
class Solution {
public:
    
    int numPairsDivisibleBy60(vector<int>& time) {
        vector<int>rem(61,0);
        int cnt=0;
        for(int &t:time){
            int curr_rem=t%60;
            cnt+=0-curr_rem>=0?rem[0-curr_rem]:0;
            cnt+=60-curr_rem>=0?rem[60-curr_rem]:0;
            rem[curr_rem]++;
        }
        return cnt;
    }
};

//int numPairsDivisibleBy60(vector<int>& time) {
//     //Notice that 1<=time[i]<=500. now the max pair sum can be 1000. Now since the pair sum needs to be divisible by 60, there are only a few nos <=1000 that are divisible by 60. So for each time[i], check how many corres partners do we have such that we can attain a one the target sums(something from array options)  
//     unordered_map<int,int>Map;//Can't use unordered_set since we need the freq of occurence as well.
//     vector<int>options({60,120,180,240,300,360,420,480,540,600,660,720,780,840,900,960});//since the pair sum can from 2 to 1000
//     int cnt=0;
//     int n=time.size();
//     for(int &t:time){
//         for(int &opt:options){
//             if(Map.find(opt-t)!=Map.end())
//                 cnt+=Map[opt-t];
//         }
//         Map[t]++;;
//     }
//     return cnt;
// }

