# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def dfs(root):
            if root is None:
                return True, 0
            l, lcnt = dfs(root.left)
            r, rcnt = dfs(root.right)
            if not (l and r):
                return False, 0
            return (abs(lcnt - rcnt) <= 1), max(lcnt, rcnt) + 1
            
        res, _ = dfs(root)
        return res