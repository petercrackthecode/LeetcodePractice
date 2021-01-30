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
class Solution {
public:
    class Vertex {
        public:
            TreeNode* node;
            int x;
            int y;
            Vertex(TreeNode* _node, int _x, int _y) {
                node = _node;
                x = _x;
                y = _y;
            }
    };
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector < vector < int > > ans;
        if(!root)
            return ans;

        vector < Vertex > sorted;
        queue < Vertex > q;
        
        q.push(Vertex(root, 0,0));
        while(!q.empty()) {
            Vertex cur = q.front(); q.pop();
            sorted.push_back(Vertex(cur.node, cur.x, cur.y));
            if(cur.node->left) 
                q.push(Vertex(cur.node->left, cur.x-1, cur.y+1));
            if(cur.node->right) 
                q.push(Vertex(cur.node->right, cur.x+1, cur.y+1));               
        }
        
        auto cmp = []  (Vertex const& a, Vertex const& b) -> bool{
            return (a.x < b.x || (a.x == b.x && a.y < b.y) || 
                    (a.x == b.x && a.y == b.y && a.node->val <= b.node->val));
        };
        sort(sorted.begin(), sorted.end(), cmp);
        
        int index = sorted[0].x;
        vector < int > num;
        for(auto i : sorted) {
            if(index < i.x) {
                ans.push_back(num);
                num.clear();
                index = i.x;
            }
            num.push_back(i.node->val);
        }
         ans.push_back(num);
        return ans;
    }
};