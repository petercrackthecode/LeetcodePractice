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

typedef ListNode* ll;

class Solution {
public:
    auto putNodeInRightPosition(ll &linkedList, ll node) -> void {
        if (!linkedList || linkedList->val >= node->val) {
            node->next = linkedList;
            linkedList = node;
        }
        else {
            ll traversalNode = linkedList,
               parentNode = nullptr;
            while (traversalNode && traversalNode->val < node->val) {
                parentNode = traversalNode;
                traversalNode = traversalNode->next;
            }
            
            parentNode->next = node;
            node->next = traversalNode;
        }
    }
    
    ListNode* insertionSortList(ListNode* head) {
        ll sortedList = nullptr,
           traversalNode = head,
           tempNode = nullptr;
        
        while (traversalNode) { // travel through the linked list until reaching an empty node
            tempNode = new ListNode(traversalNode->val);
            putNodeInRightPosition(sortedList, tempNode);
            traversalNode = traversalNode->next;
        }
        
        return sortedList;
    }
};