// link: https://leetcode.com/problems/validate-binary-search-tree/
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
class Solution {
private:
    TreeNode* prev=NULL;
public:
    bool isValidBST(TreeNode* root) {
        if(!root)   return true;
        return isValidBST(root->left)  && help(root) && isValidBST(root->right);
    }
    
    bool help(TreeNode* root){
        if(!prev){
            prev=root;
            return true;
        }
        if(prev->val >= root->val)   return false;
        prev=root;
        return true;
    }
};