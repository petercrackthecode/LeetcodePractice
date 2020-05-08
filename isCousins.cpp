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

void recursiveTraversal(TreeNode * node, const int &x, const int &y, int &xDepth, int &yDepth, std::stack<int> &values) {
	
}

bool checkBasicCondition(TreeNode * root, int x, int y) {
	if (root == nullptr || x == y || root->val == x || root->val == y)
		return false;
	else if (root->left != nullptr && (root->left->val == x || root->left->val == y))
		return false;
	else if (root->right != nullptr && (root->right->val == x || root->right->val == y))
		return false;

	return true;
}

bool isCousins(TreeNode* root, int x, int y) {
	int xDepth{2},
	    yDepth{2};
	std::stack<TreeNode*> values;
	TreeNode * tempNode= root;
	int currDepth{0};
	bool foundXorY{false};

	if (!checkBasicCondition(root, x, y))
		return false;
	
	while (!foundXorY && !(values.empty() && tempNode == nullptr)) {
		while (tempNode && !foundXorY) {
			values.push(tempNode);
			if (tempNode->val == x || tempNode.val == y) {
				if (tempNode.val == x) {
					xDepth = currDepth;
				}
				else yDepth= currDepth;

				foundXorY= true;
			}
			else {
				tempNode= tempNode-left;
				++currDepth;
			}
		}
	}
}

// M
// N