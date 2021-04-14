// link: https://leetcode.com/problems/partition-list/

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
private:
    auto addToNode(ListNode * &node, ListNode * &temp, const int &val) -> void {
        if (!node) {
            node = new ListNode(val);
            temp = node;
        }
        else {
            temp->next = new ListNode(val);
            temp = temp->next;
        }
    }
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode *smaller = nullptr,
                 *smallerTemp = nullptr,
                 *greater = nullptr,
                 *greaterTemp = nullptr;
        
        ListNode * temp = head;
        while (temp) {
            if (temp->val < x) {
                addToNode(smaller, smallerTemp, temp->val);
            }
            else addToNode(greater, greaterTemp, temp->val);
            
            temp = temp->next;
        }
        
        if (!smaller)
            smaller = greater;
        else smallerTemp->next = greater;
        
        return smaller;
    }
};