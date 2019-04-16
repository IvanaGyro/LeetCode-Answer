# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, None, None)
        
    def dfs(self, root, lo, hi):
        if root is None:
            return True
        if lo is not None and root.val <= lo:
            return False
        if hi is not None and root.val >= hi:
            return False
        return self.dfs(root.left, lo, root.val) and self.dfs(root.right, root.val, hi)
            