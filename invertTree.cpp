// link: https://leetcode.com/problems/invert-binary-tree/
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
    void swap(TreeNode *&firstNode, TreeNode *&secondNode) {
        TreeNode *temp = firstNode;
        firstNode = secondNode;
        secondNode = temp;
    }

    void invertTreeRecursively(TreeNode *&node) {
    	if (node) {
    		invertTreeRecursively(node->left);
    		invertTreeRecursively(node->right);
    		swap(node->left, node->right);
    	}
    }

    void invertTreeIteratively(TreeNode *node) {
    	
    }

    TreeNode *invertTree(TreeNode *root) {
        invertTreeRecursively(root);
        return root;
    }
};