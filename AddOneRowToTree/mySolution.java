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
    void addOneRow(LinkedList<TreeNode> q, int v) {
        TreeNode popped = null;
        
        while (!q.isEmpty()) {
            TreeNode newLeft = new TreeNode(v),
                     newRight = new TreeNode(v);
            popped = q.poll();
            newLeft.left = popped.left;
            newRight.right = popped.right;
            popped.left = newLeft;
            popped.right = newRight;
        }
    }
    
    public TreeNode addOneRow(TreeNode root, int v, int d) {
        if (d == 1) {
            TreeNode node = new TreeNode(v);
            node.left = root;
            root = node;
        }
        else {
            int level = 1;
            LinkedList<TreeNode> q1 = new LinkedList<>(),
                                 q2 = new LinkedList<>();
            
            TreeNode popped = null;
            
            q1.add(root);
            while (level < d - 1) {
                if (!q1.isEmpty()) {
                    while (!q1.isEmpty()) {
                        popped = q1.poll();
                        if (popped.left != null) q2.push(popped.left);
                        if (popped.right != null) q2.push(popped.right);
                    }
                    ++level;
                }
                else if (!q2.isEmpty()) {
                    while (!q2.isEmpty()) {
                        popped = q2.poll();
                        if (popped.left != null) q1.push(popped.left);
                        if (popped.right != null) q1.push(popped.right);
                    }
                    
                    ++level;
                }
            }
            
            if (!q1.isEmpty())
                addOneRow(q1, v);
            else addOneRow(q2, v);
        }
        
        return root;
    }
}