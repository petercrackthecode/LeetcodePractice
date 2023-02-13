// link: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3292/

#include <vector>
#include <algorithm>

class MinStack {
public:
    /** initialize your data structure here. */
    std::vector<int> data;
    int min;
    
    MinStack() {
        min= INT_MAX;
    }
    
    void push(int x) {
        data.push_back(x);
        if (x < min) {
            min= x;
        }
    }
    
    void pop() {
        data.pop_back();
        if (data.size() == 0) min= INT_MAX;
        else min= *min_element(data.begin(), data.end());
    }
    
    int top() {
        if (data.size() == 0)
            return INT_MIN;
        return data[data.size() - 1];
    }
    
    int getMin() {
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */