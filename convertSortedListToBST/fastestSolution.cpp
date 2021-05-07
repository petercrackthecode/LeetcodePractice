// link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
	auto sortedListToBST(ListNode* head) -> TreeNode * {
		vector<int> vals;
		
		auto node = head;
		while (node) {
			vals.push_back(node->val);
			node = node->next;
		}

		return helper(vals, 0, vals.size() - 1);
	}

	auto helper(const vector<int>& vals, int l, int r) -> TreeNode * {
		if (l > r)
			return nullptr;

		int m = (l + r)/2;
		auto node = new TreeNode(vals[m]);

		if (l < r) {
			node->left = helper(vals, l, m-1);
			node->right = helper(vals, m+1, r);
		}

		return node;
	}
};