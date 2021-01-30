// link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

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
typedef map<int, vector<TreeNode *>> mivtn;
typedef vector<vector<int>> vvi;

class Solution {
private:
    mivtn nodesValuesBasedOnVerticalOrder;
    map<TreeNode *, int> nodesRow;
public:
    auto verticalTraversalRecursive(TreeNode* node, const int &verticalOrder, const int &row) -> void {
        if (!node)
            return;
        
        nodesValuesBasedOnVerticalOrder[verticalOrder].push_back(node);
        nodesRow[node] = row;
        
        verticalTraversalRecursive(node->left, verticalOrder - 1, row + 1);
        verticalTraversalRecursive(node->right, verticalOrder + 1, row + 1);
    }
    
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vvi ans;
        int verticalOrder = 0,
            row = 0;
        
        verticalTraversalRecursive(root, verticalOrder, row);
        
        for (auto &[currentVerticalOrder, nodesOnSameVerticalOrder] : nodesValuesBasedOnVerticalOrder) {
            vector<int> translatedArray;
            
            std::sort(nodesOnSameVerticalOrder.begin(), nodesOnSameVerticalOrder.end(), [=](TreeNode * a, TreeNode * b) -> bool {
                if (nodesRow[a] < nodesRow[b]) {
                    return true;
                }
                else if (nodesRow[a] > nodesRow[b]) {
                    return false;
                }
                else {
                    return a->val < b->val;
                }
            });
            
            for (auto node : nodesOnSameVerticalOrder) {
                translatedArray.push_back(node->val);
            }
            
            ans.push_back(translatedArray);
        }
        
        return ans;
    }
};