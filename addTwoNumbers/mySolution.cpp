/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
typedef ListNode * ln;

class Solution {
public:
    static auto addTwoStringAndSaveToALinkedList(const string &s1, const std::string &s2, ln &node) -> void {
        bool addOneToNextAddition = false;
        
        int s1Index = s1.length() - 1,
            s2Index = s2.length() - 1,
            currentDigitsSum = 0;
        
        ln traversalNode = node;
        
        while (s1Index >= 0 || s2Index >= 0) {
            if (s1Index < 0) {
                currentDigitsSum = 0 + (s2[s2Index] - '0');
                --s2Index;
            }
            else if (s2Index < 0) {
                currentDigitsSum = 0 + (s1[s1Index] - '0');
                --s1Index;
            }
            else {
                currentDigitsSum = (s1[s1Index] - '0') + (s2[s2Index] - '0');
                --s1Index;
                --s2Index;
            }
            
            if (addOneToNextAddition)
                ++currentDigitsSum;
            
            if (currentDigitsSum < 10) {
                addOneToNextAddition = false;
            }
            else {
                addOneToNextAddition = true;
                currentDigitsSum %= 10;
            }
            
            // add the digit to node
            if (!node) {
                node = new ListNode(currentDigitsSum);
                traversalNode = node;
            }
            else {
                traversalNode->next = new ListNode(currentDigitsSum);
                traversalNode = traversalNode->next;
            }
        }
        
        if (addOneToNextAddition) {
            if (!node) {
                node = new ListNode(1);
                traversalNode = node;
            }
            else {
                traversalNode->next = new ListNode(1);
                traversalNode = traversalNode->next;
            }
        }
    }
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        /* 1. Extract all the digits from l1 into a string, call it s1.
              Reverse s1.
           2. Extract all the digits from l2 into a string, call it s2.
              Reverse s2.
           3. Add s1 and s2 together digit by digit, from right to left (from the digits with lowest significance to the highest)
           4. Save the result into a string called result. Reverse result.
           5. Save all the digits of result into a linked list.
        */
        
        std::string s1 = "",
                    s2 = "";
        
        ln traversalNode = l1,
           ans = nullptr;
        
        while (traversalNode) {
            s1 = std::to_string(traversalNode->val) + s1;
            traversalNode = traversalNode->next;
        }
        
        traversalNode = l2;
        
        while (traversalNode) {
            s2 = std::to_string(traversalNode->val) + s2;
            traversalNode = traversalNode->next;
        }
        
        addTwoStringAndSaveToALinkedList(s1, s2, ans);
        
        return ans;
    }
};