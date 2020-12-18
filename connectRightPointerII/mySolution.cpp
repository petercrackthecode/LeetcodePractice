// link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/
class Solution {
public:
    auto connectRecursive(Node * parent) -> void {
        if (!parent)
            return;
        
        Node * leftMostChild = nullptr,
             * moveFrom = nullptr;
        while (parent) {
            if (parent->left && parent->right) {
                if (!leftMostChild)
                    leftMostChild = parent->left;
                
                if (moveFrom)
                    moveFrom->next = parent->left;
                
                parent->left->next = parent->right;
                moveFrom = parent->right;
            }
            else if (parent->left || parent->right) {
                if (!leftMostChild)
                    leftMostChild = (parent->left) ? parent->left : parent->right;
                
                if (moveFrom)
                    moveFrom->next = (parent->left) ? parent->left : parent->right;
                moveFrom = (parent->left) ? parent->left : parent->right;
            }
            
            parent = parent->next;
        }
        
        connectRecursive(leftMostChild);
    }
    
    Node* connect(Node* root) {
        connectRecursive(root);
        
        return root;
    }
    
    
};