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
    int maxD = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        getHeight(root);
            return maxD;
    }
        private int getHeight(TreeNode node){
            if(node==null) return 0;
            int leftH = getHeight(node.left);
            int rightH = getHeight(node.right);
            maxD =  Math.max(maxD, leftH + rightH);
        
        return 1+ Math.max(leftH , rightH);
        
    }
}