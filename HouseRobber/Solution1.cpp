// link: https://leetcode.com/problems/house-robber-iii/

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
    int rob(TreeNode* root) {
        int level = 1;
        
        int evenNumHousesRevenue = 0,
            oddNumHousesRevenue = 0;
        
        queue<TreeNode *> nodes,
                          secondNodes;
        TreeNode * current = nullptr;
        
        nodes.push(root);
        
        while (!nodes.empty() || !secondNodes.empty()) {
            if (nodes.empty()) {
                nodes = secondNodes;
                secondNodes = queue<TreeNode *>();
                ++level;
            }
            
            while (!nodes.empty()) {
                current = nodes.front();
                nodes.pop();
                
                if (!current)
                    continue;
                
                if (current->left)
                    secondNodes.push(current->left);
                if (current->right)
                    secondNodes.push(current->right);
                
                (level % 2 == 0) ? (evenNumHousesRevenue += current->val)
                                 : (oddNumHousesRevenue += current->val);
            }
        }
        
        return max(evenNumHousesRevenue, oddNumHousesRevenue);
    }
};