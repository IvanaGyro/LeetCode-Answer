# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        root.max = root.val
        root.min = root.val
        ans = 0
        
        def dfs(node):
            nonlocal ans
            ans = max(abs(node.max - node.val), abs(node.min - node.val), ans)
            c_max = max(node.max, node.val)
            c_min = min(node.min, node.val)
            if node.left is not None:
                node.left.max = c_max
                node.left.min = c_min
                dfs(node.left)
            if node.right is not None:
                node.right.max = c_max
                node.right.min = c_min
                dfs(node.right)
                
        dfs(root)
                
        return ans
        