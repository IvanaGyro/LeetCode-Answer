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
var longestUnivaluePath = function(root) {
    var findLongestUnivaluePath = function(root) {
        if (root.left === null && root.right === null) return [0, 0, 0];
        
        var leftResult, rightResult;
        var result = [0, 0, 0];
        if (root.left !== null) {
            leftResult = findLongestUnivaluePath(root.left);
            if (root.val == root.left.val) {
                result[0] = leftResult[0];
                result[1] = leftResult[2] + 1;
                result[2] = result[1];
            } else {
                result[0] = leftResult[0] > leftResult[1] ? leftResult[0] : leftResult[1];
            }
        }
        if (root.right !== null) {
            rightResult = findLongestUnivaluePath(root.right);
            if (root.val == root.right.val) {
                result[0] = rightResult[0] > result[0] ? rightResult[0] : result[0];
                result[1] += rightResult[2] + 1;
                result[2] = result[2] > rightResult[2] + 1 ? result[2] : rightResult[2] + 1;
            } else {
                result[0] = Math.max(rightResult[0], rightResult[1], result[0]);
            }
        }
        
        return result;
    }
    
    if (root === null) return 0;
    var result = findLongestUnivaluePath(root);
    return result[0] > result[1] ? result[0] : result[1];

};