// link: https://leetcode.com/problems/linked-list-cycle/

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
    bool hasCycle(ListNode *head) {
        if (!head || !head->next)
            return false;
        
        ListNode * moveTwoSteps = head,
                 * moveOneStep = head;
        
        moveTwoSteps = (moveTwoSteps->next)->next;
        moveOneStep = moveOneStep->next;
        
        while (moveTwoSteps) {
            if (moveTwoSteps->next == moveOneStep)
                return true;
            moveTwoSteps = moveTwoSteps->next;
            if (moveTwoSteps && moveTwoSteps->next == moveOneStep)
                return true;
            if (moveTwoSteps)
                moveTwoSteps = moveTwoSteps->next;
            
            moveOneStep = moveOneStep->next;
        }
        
        return false;
    }
};