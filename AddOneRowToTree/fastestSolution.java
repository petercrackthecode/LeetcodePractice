// link: https://leetcode.com/problems/add-one-row-to-tree/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode addOneRow(TreeNode root, int v, int d) {
        if(d == 1){
            TreeNode a = new TreeNode(v);
            a.left = root;
            return a;
        }
        help(root , v , d);
        return root;
    }
    
    void help(TreeNode root , int v , int d){
        if(root == null){
            return ;
        }
        if(d-1 == 1){
            TreeNode a1 = new TreeNode(v);
            TreeNode a2 = new TreeNode(v);
            TreeNode  s = root.left;
            TreeNode s1 = root.right;
            root.left = a1;
            a1.left = s;
            root.right = a2;
            a2.right = s1;
            return ;
        }
        help(root.left  , v , d-1);
        help(root.right , v ,d-1);
    }
}