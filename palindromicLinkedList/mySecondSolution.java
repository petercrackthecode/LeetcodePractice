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
        LinkedList<ListNode> nodes = new LinkedList();
        ListNode temp = head;
        while (temp != null) {
            nodes.add(temp);
            temp = temp.next;
        }
        
        int half = nodes.size() / 2;
        temp = head;
        
        while (half > 0) {
            if (temp.val != nodes.peekLast().val)
                return false;
            temp = temp.next;
            nodes.pollLast();
            --half;
        }
        
        return true;
    }
}