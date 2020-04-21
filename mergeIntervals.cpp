// link: https://leetcode.com/problems/merge-intervals/
bool myComparator (std::vector<int> first, std::vector<int> second) { 
    return (first[0] < second[0]); 
}

std::vector<std::vector<int>> merge(std::vector<std::vector<int>>& meetings)
{
    // merge meeting ranges 
    std::vector<std::vector<int>> mergedMeetings;
                    
    std::sort(meetings.begin(), meetings.end(), myComparator);
    
    int index{0};
    
    while (index < meetings.size()) {
        std::vector<int> aMeeting= meetings[index];
        if (index != meetings.size() - 1) {
            while (index < meetings.size() - 1 && aMeeting[1] >= meetings[index + 1][0]) {
                if (aMeeting[1] < meetings[index + 1][1]) {
                    aMeeting[1]= meetings[index + 1][1];
                }
                ++index;
            }
        }
        mergedMeetings.push_back(aMeeting);
        ++index;
    }

    return mergedMeetings;
}