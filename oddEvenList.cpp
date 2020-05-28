// link: https://leetcode.com/problems/odd-even-linked-list/
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
 ListNode* oddEvenList(ListNode* head) {
    if (!head || !head->next || !head->next->next) {
        return head;
    }
        
    ListNode * lastOddOrderedNode= head,
               lastEvenOrderedNode= head->next;

    int numberTracker{1};
}