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
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* newNode, *temp;
        if(l1 == NULL)
            return l2;
        else if (l2 == NULL)
            return l1;
        else if(l1->val < l2->val)
        {
            newNode = l1;
            l1 = l1->next;
            temp = newNode;
        }
        else
        {
            newNode = l2;
            l2 = l2->next;
            temp = newNode;
        }
        while(l1 != NULL && l2 != NULL)
        {
            if(l1->val < l2->val)
            {
                temp->next= l1;
                l1=l1->next;
            }
            else 
            {
                temp->next = l2;
                l2 = l2->next;
            }
            temp = temp->next;
        }
        while(l1 != NULL)
        {
            temp->next = l1;
            l1 = l1->next;
            temp = temp->next;
        }
        while(l2 != NULL)
        {
            temp->next = l2;
            l2 = l2->next;
            temp = temp->next;
        }
        return newNode;
    }
};