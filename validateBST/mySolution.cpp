//  link: https://leetcode.com/problems/validate-binary-search-tree/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
typedef TreeNode * tn;

class Solution {
public:
    bool isValidBstRecursive(tn root, int &lastVal, bool &isLastValInitialized) {
        if (!root)
            return true;

        
        if (!isValidBstRecursive(root->left, lastVal, isLastValInitialized)) {
            return false;
        }
        
        
        if (!isLastValInitialized) {
            lastVal = root->val;
            isLastValInitialized = true;
        }
        else {
            if (lastVal >= root->val) {
                return false;
            }
            else {
                lastVal = root->val;
            }
        }
        
        if (!isValidBstRecursive(root->right, lastVal, isLastValInitialized)) {
            return false;
        }
        
        return true;
    }
    
    bool isValidBST(TreeNode* root) {
        int lastVal = INT_MIN;
        
        bool isLastValInitialized = false;
        
        return isValidBstRecursive(root, lastVal, isLastValInitialized);
    }
};

// inorder traversal
// save the last value to a variable - lastVal
// everytime you move to a new node, see if that node is greater than lastVal:
//      - if yes, keep going.
//      - if no, return false, terminate immediately.
// When the traversal ends smoothly, return true.