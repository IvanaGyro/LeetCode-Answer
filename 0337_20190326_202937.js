/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var rob = function(root) {
    if (root === null) return 0;
    if (root.left === null & root.right === null) return root.val;
    if (root.max !== undefined) return root.max;
    var max1 = 0, // root is broken into
        max2 = 0; // root is not broken into
    
    var rob_child = function(child) {
        if (child !== null) {
            if (child.left !== null) {
                max1 += rob(child.left);    
            }
            if (child.right !== null) {
                max1 += rob(child.right);
            }
            max2 += rob(child);
        }
    };
    
    rob_child(root.left);
    rob_child(root.right);
    
    root.max = Math.max(max1 + root.val, max2);
    return root.max;
};