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
/* 1. Traverse through the tree recursively (both left and right)
   2. Everytime we step on a new node:
        If the node hasn't shown up in the map, ++map[node->val], ++oddAppearancesCount
        If the node has shown up in the map once, ++map[node->val], --oddAppearancesCount
        If the node has shown up in the map more than twice ++map[node->val], terminate the recursion immediately.
   3. If the node is a leaf node:
        If oddAppearancesCount <= 1, ++ans;
   4. --map[node->val] after we are done with it (after the recursive function calls).
*/
typedef TreeNode * tn;
typedef map<int, int> mii;

class Solution {
public:
    void pseudoPalindromicPathsRecursive(tn root, mii frequencies, int &ans, int oddAppearancesCount) {
        if (!root)
            return;
        
        ++frequencies[root->val];
        if (frequencies[root->val] % 2 == 1) {
            ++oddAppearancesCount;
        }
        else {
            --oddAppearancesCount;
        }
        
        if (!root->left && !root->right) {
            if (oddAppearancesCount <= 1)
                ++ans;
        }
        else {
            if (root->left)
                pseudoPalindromicPathsRecursive(root->left, frequencies, ans, oddAppearancesCount);
            if (root->right)
                pseudoPalindromicPathsRecursive(root->right, frequencies, ans, oddAppearancesCount);
        }
    }
    
    int pseudoPalindromicPaths (TreeNode* root) {
        mii frequencies;
        int ans = 0,
            oddAppearancesCount = 0;
        pseudoPalindromicPathsRecursive(root, frequencies, ans, 0);
        
        return ans;
    }
};