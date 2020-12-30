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
public:
    
    int c=0;
    
    void dfs(TreeNode *root, int odd){
        
        if(!root)
            return;
        
        odd ^= (1<<root->val);
        
        if(!root->left && !root->right && __builtin_popcount(odd)<2)
            c++;
            
        dfs(root->left, odd);
        dfs(root->right, odd);
    }
    
    int pseudoPalindromicPaths (TreeNode* root) {
        
        int odd=0;
        dfs(root, odd);
        return c;
    }
};