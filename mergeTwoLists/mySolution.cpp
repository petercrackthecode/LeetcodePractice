// link: https://leetcode.com/problems/merge-two-sorted-lists/

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
    static auto addNode(ln &answer, ln &travel_answer, ln nodeToAdd) -> void {
        if (!answer) {
            answer = nodeToAdd;
            travel_answer = answer;
        }
        else {
            travel_answer->next = nodeToAdd;
            travel_answer = travel_answer->next;
        }
    }
    
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ln travel_l1 = l1,
           travel_l2 = l2,
           answer = nullptr,
           travel_answer = answer;
        
        while (travel_l1 && travel_l2) {
            if (travel_l1->val < travel_l2->val) {
                addNode(answer, travel_answer, travel_l1);
                travel_l1 = travel_l1->next;
            }
            else {
                addNode(answer, travel_answer, travel_l2);
                travel_l2 = travel_l2->next;
            }
        }
        
        while (travel_l1) {
            addNode(answer, travel_answer, travel_l1);
            travel_l1 = travel_l1->next;
        }
        
        while (travel_l2) {
            addNode(answer, travel_answer, travel_l2);
            travel_l2 = travel_l2->next;
        }
        
        return answer;
    }
};