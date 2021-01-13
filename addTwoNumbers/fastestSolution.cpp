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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* s = nullptr;
        ListNode** c = &s;
        ListNode* cl1 = l1;
        ListNode* cl2 = l2;
        int next = 0;
        while (cl1 != nullptr || cl2 != nullptr || next != 0) {
            *c = new ListNode();
            (*c)->val = (cl1 ? cl1->val : 0) + (cl2 ? cl2->val : 0) + next;
            next = 0;
            if ((*c)->val > 9) {
                (*c)->val -= 10;
                next = 1;
            }
            c = &((*c)->next);
            cl1 = cl1 ? cl1->next : cl1;
            cl2 = cl2 ? cl2->next : cl2;
        }
        return s;
    }
};