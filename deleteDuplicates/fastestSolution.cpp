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
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        while(head && head->next && head->val == head->next->val){
            int val = head->val;
            while(head && head->val == val){
                ListNode* t = head;
                head = head->next;
                delete t;
            }
        }
        ListNode* t = nullptr, *l = nullptr;
        if(head) l = head, t = head->next;
        while(t){
            if(t && t->next && t->val == t->next->val){
                int val = t->val;
                while(t && t->val == val){
                    ListNode* tmp = t;
                    t = t->next;
                    delete tmp;
                }
                l->next = t;
                
            }
            else {
                l = t;
                t = t->next;
            }
        }
        
        
        return head;
    }
};