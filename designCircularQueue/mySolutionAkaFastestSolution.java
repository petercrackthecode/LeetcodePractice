// link: https://leetcode.com/problems/design-circular-queue/
class Node {
    public int val;
    public Node next;
    
    public Node() {
        val = 0;
        next = null;
    }
    
    public Node(int _val) {
        val = _val;
        next = null;
    }
}

class MyCircularQueue {
    private Node head = null, tail = null;
    private int maxSize = 0,
                currSize = 0;
    
    public MyCircularQueue(int k) {
        maxSize = k;
    }
    
    public boolean enQueue(int value) {
        if (isFull())
            return false;
        
        if (head == null) {
            head = new Node(value);
            head.next = head;
            tail = head; 
        }
        else {
            Node temp = new Node(value);
            temp.next = head;
            tail.next = temp;
            tail = temp;
        }
        
        ++currSize;
        
        return true;
    }
    
    public boolean deQueue() {
        if (isEmpty())
            return false;
        
        if (head == tail) {
            head = null;
            tail = null;
        }
        else {
            head = head.next;
            tail.next = head;
        }
        --currSize;
        
        return true;
    }
    
    public int Front() {
        if (isEmpty())
            return -1;
        
        return head.val;
    }
    
    public int Rear() {
        if (isEmpty())
            return -1;
        
        return tail.val;
    }
    
    public boolean isEmpty() {
        return currSize == 0;
    }
    
    public boolean isFull() {
        return maxSize == currSize;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */