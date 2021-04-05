// link: https://leetcode.com/problems/palindrome-linked-list/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null)
            return true;
        int length = 0;
        ListNode temp = head;
        
        while (temp != null) {
            ++length;
            temp = temp.next;
        }
        
        ListNode lastNode = null,
                 nextNode = null;
        
        int half = length / 2;
        temp = head;
        if (length % 2 == 0) {
            for (int index = 0; index < half - 1; ++index)
                temp = temp.next;
        }
        else {
            for (int index = 0; index < half; ++index)
                temp = temp.next;
        }
        
        lastNode = temp;
        nextNode = temp.next;
        
        while (nextNode != null) {
            temp = nextNode.next;
            nextNode.next = lastNode;
            lastNode = nextNode;
            nextNode = temp;
        }
        
        temp = head;
        
        while (half > 0) {
            if (lastNode.val != temp.val)
                return false;
            lastNode = lastNode.next;
            temp = temp.next;
            
            --half;
        }
        
        return true;
    }
}