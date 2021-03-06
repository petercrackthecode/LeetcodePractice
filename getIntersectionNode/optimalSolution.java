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
/*
    1. First, find out if two nodes intersect by looking if both of 'em share the same final node:
    - No: return null.
    - Yes: Move to step 2.
    2. Take the length of linkedList A and linkedList B, see which node has the greater length.
    3. Take the difference between their length, call it k.
    4. For the node with the greater length, move k steps from the beginning, so two nodes
    will reach the same point (the intersected point) if they move the same speed.
    5. Concurrently traverse through linkedList A and B by one step until their node pointers reach the same point. Return that point.
*/

public class Solution {
    private int getLength(ListNode node, ListNode temp) {
        if (node == null)
            return 0;
        
        int length = 1;
        temp = node;
        
        while (temp.next != null) {
            ++length;
            temp = temp.next;
        }
        
        return length;
    }
    
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode lastNodeOfA = null,
                 lastNodeOfB = null;
        
        int headALength = getLength(headA, lastNodeOfA),
            headBLength = getLength(headB, lastNodeOfB);
        
        if (lastNodeOfA != lastNodeOfB) {
            // two linked lists don't intersect.
            return null;
        }
        ListNode longerList = (headALength >= headBLength) ? headA : headB,
                 shorterList = (headALength < headBLength) ? headA : headB;
        
        int listLengthDiff = Math.abs(headALength - headBLength);
        
        ListNode shortListTemp = shorterList,
                 longListTemp = longerList;
        
        while (listLengthDiff > 0) {
            longListTemp = longListTemp.next;
            --listLengthDiff;
        }
        
        while (shortListTemp != longListTemp) {
            longListTemp = longListTemp.next;
            shortListTemp = shortListTemp.next;
        }
        
        return longListTemp;
    }
}