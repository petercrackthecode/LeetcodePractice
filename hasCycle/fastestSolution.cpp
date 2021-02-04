// link: https://leetcode.com/problems/linked-list-cycle/

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL)
   	    	return false;
        ListNode *slow=head,*fast = head;
    	    while(slow && fast && fast->next)
    	    {
    	    	
			slow = slow ->next;
    	    fast = fast->next->next;
    	    if(slow == fast)
    	    	return true;
    	    else
    	    	continue;
    	    
    	}
    	return false;
        
        
    }
};