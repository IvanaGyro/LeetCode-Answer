# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        levels = []
        def dfs(root, level):
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)
            if not root.left and not root.right:
                levels.append(level)
                
        dfs(root, 1)
        return min(levels)