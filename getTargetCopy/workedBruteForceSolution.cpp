/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

typedef TreeNode * tn;

class Solution {
public:
    // Brute-force solution:
    // 1. Search all the elements in the cloned tree using bfs/dfs, return the node with the same value as the target node.
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        queue<tn> nodes;
        nodes.push(cloned);
        
        tn toBeFoundNode = nullptr;
        
        while (!nodes.empty()) {
            if (nodes.front()->val == target->val) {
                toBeFoundNode = nodes.front();
                break;
            }
            
            if (nodes.front()->left)
                nodes.push(nodes.front()->left);
            if (nodes.front()->right)
                nodes.push(nodes.front()->right);
            
            nodes.pop();
        }
        
        return toBeFoundNode;
    }
};