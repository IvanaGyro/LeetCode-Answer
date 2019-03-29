/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    if (root === null) return '[]';
    var arr = [],
        last = 0;
    arr.push(root);
    while(last != arr.length) {
        let len = arr.length;
        while(last < len) {
            let node = arr[last];
            if (node !== null) {
                arr.push(node.left);
                arr.push(node.right);
            }
            ++last;
        }
    }
    arr.forEach((val, idx, arr)=>{
        if (val !== null) {
            arr[idx] = arr[idx].val;
        }
    });
    return JSON.stringify(arr);
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    var arr = JSON.parse(data);
    if (arr.length == 0) return null;
    
    var ptr = 0;
    arr[0] = new TreeNode(arr[0]);
    
    for (let i = 0; i < arr.length; ++i) {
        if (arr[i] !== null) {
            if (++ptr < arr.length) {
                arr[ptr] = arr[ptr] === null ? null : new TreeNode(arr[ptr]);
                arr[i].left = arr[ptr];
            } else {
                arr[i].left = null;
            }
            if (++ptr < arr.length) {
                arr[ptr] = arr[ptr] === null ? null : new TreeNode(arr[ptr]);
                arr[i].right = arr[ptr];
            } else {
                arr[i].right = null;
            }
        }
    }

    return arr[0];
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */