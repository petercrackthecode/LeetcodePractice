// link: https://leetcode.com/problems/intersection-of-two-linked-lists/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        HashMap<ListNode, Boolean> headADictionary = new HashMap<ListNode, Boolean>();
        
        ListNode temp = headA;
        
        while (temp != null) {
            headADictionary.put(temp, true);
            temp = temp.next;
        }
        
        temp = headB;
        
        while (temp != null) {
            if (headADictionary.containsKey(temp))
                return temp;
            temp = temp.next;
        }
        
        return null;
    }
}