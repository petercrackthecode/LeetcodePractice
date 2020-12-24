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
typedef ListNode * ll;

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next)
            return head;
        
        ll traversalNode = head,
           lastTraversalNode = nullptr,
           first,
           second;
        
        while (traversalNode) {
            first = traversalNode;
            second = traversalNode->next;
            
            if (!second)
                break;
            
            first->next = second->next;
            second->next = first;
            if (!lastTraversalNode) {
                head = second;
            }
            
            if (lastTraversalNode) {
                lastTraversalNode->next = second;
            }
            
            lastTraversalNode = traversalNode;
            traversalNode = traversalNode->next;
        }
        
        return head;
    }
};