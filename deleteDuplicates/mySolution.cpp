// link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

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

typedef ListNode* ln;

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ln lastNode = nullptr,
           traversingNode = head;
        
        while (traversingNode) {
            if (traversingNode->next && traversingNode->val == traversingNode->next->val) {
                while (traversingNode->next && traversingNode->val == traversingNode->next->val)
                    traversingNode = traversingNode->next;
                
                if (!lastNode)
                    head = traversingNode->next;
                else lastNode->next = traversingNode->next;
                
                traversingNode = traversingNode->next;
            }
            else {
                lastNode = traversingNode;
                traversingNode = traversingNode->next;
            }
        }
        
        return head;
    }
};