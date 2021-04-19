// link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length = 0;
        ll temp = head;
        
        while (temp) {
            ++length;
            temp = temp->next;
        }
        
        ll parent = nullptr,
           child = head;
        
        while (length != n) {
            parent = child;
            child = child->next;
            --length;
        }
        
        // deleting the first node
        if (child == head) {
            temp = head;
            head = head->next;
            delete temp;
        }
        else {
            parent->next = child->next;
            delete child;
        }
        
        return head;
    }
};