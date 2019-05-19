# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        from math import inf
        
        if not root:
            return 0
        
        def dfs(root):
            if not root:
                return -inf, -inf, -inf
            l_sinc, l_tinc, l_exc = dfs(root.left)
            r_sinc, r_tinc, r_exc = dfs(root.right)
            
            sinc = root.val + max(l_sinc, r_sinc, 0)
            tinc = root.val + max(l_sinc, r_sinc, l_sinc + r_sinc, 0)
            exc = max(l_tinc, l_exc, r_tinc, r_exc)
            
            return sinc, tinc, exc
        
        return max(dfs(root))
    