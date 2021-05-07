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
typedef vector<int> vi;

class Solution {
    vi nums;
    auto sortedListToBSTHelper(const int& left, const int& right) -> TreeNode * {
        if (left > right || left < 0 || right >= nums.size())
            return nullptr;
        
        int mid = left + (right - left)/2;
        
        TreeNode * node = new TreeNode(nums[mid]);
        node->left = sortedListToBSTHelper(left, mid - 1);
        node->right = sortedListToBSTHelper(mid + 1, right);
        
        return node;
    }
public:
    TreeNode* sortedListToBST(ListNode* head) {
        // convert head linked-list into an array to access the values more easily;
        while (head) {
            nums.push_back(head->val);
            head = head->next;
        }
        TreeNode * ans = nullptr;
        
        int left = 0,
            right = nums.size() - 1;
        
        ans = sortedListToBSTHelper(left, right);
        
        return ans;
    }
};