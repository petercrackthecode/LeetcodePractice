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
    void processChild(Node *node, Node *&child, Node *&firstChild){
        if(node){
            if(firstChild){
                child->next = node;
                child = node;
            }
            else{
                firstChild = node;
                child = node;
            }
        }
    }
    
    Node* connect(Node* root) {
        Node *firstChild = root;
        
        while(firstChild){
            Node *parent = firstChild;
            firstChild = nullptr;
            Node *child = nullptr;
            while(parent){
                processChild(parent->left, child, firstChild);
                processChild(parent->right, child, firstChild);
                parent = parent->next;
            }
        }
        
        return root;
    }
};