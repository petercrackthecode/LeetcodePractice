// link: https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter {
    std::vector<int> requests;
public:
    RecentCounter() {
                
    }
    
    int ping(int t) {
        requests.push_back(t);
        int startTime = t - 3000;
        if (startTime <= requests[0])
            return static_cast<int>(requests.size());
        int low = 0,
            high = requests.size() - 1,
            mid = (high - low) / 2;
        bool found = false;

        while (low <= high && !found)   {
            if (requests[mid] >= startTime && requests[mid - 1] <= startTime) {
                if (requests[mid - 1] == startTime)
                    --mid;
                found = true;
                continue;
            }
            else if (startTime >= requests[mid]) {
                low = mid + 1;
            }
            else if (startTIme <= requests[mid - 1]) {
                high = mid - 1;
            }
            
            mid = (high - low) / 2 + low;
        }      

        return requests.size() - mid;
    }
};
