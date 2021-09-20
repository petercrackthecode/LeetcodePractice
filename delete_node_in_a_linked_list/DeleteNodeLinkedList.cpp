// link: https://leetcode.com/problems/delete-node-in-a-linked-list/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        
        if (!node || !node->next) {
            throw new std::out_of_range("Cannot delete an empty node or a tail node");
        }
        
        node->val = node->next->val;
        ListNode * deallocatedNode = node->next;
        node->next = node->next->next;
        delete deallocatedNode;
    }
};