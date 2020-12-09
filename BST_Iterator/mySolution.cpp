// link: https://leetcode.com/problems/binary-search-tree-iterator/

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
class BSTIterator {
private:
    std::queue<int> values; 
    int currentValue;
    void populateBST(TreeNode * root) {
        if (!root)
            return;
        else {
            if (root->left) populateBST(root->left);
            values.push(root->val);
            if (root->right) populateBST(root->right);
        }
    }
public:
    BSTIterator(TreeNode* root) {
        populateBST(root);
    }
    
    int next() {
        currentValue = values.front();
        values.pop();
        return currentValue;
    }
    
    bool hasNext() {
        return !values.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */