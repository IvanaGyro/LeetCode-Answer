# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root.left and not root.right:
                return root
            if root.left:
                root.left, root.right = root.right, root.left
            prev = dfs(root.right)
            if root.left:
                prev.right = root.left
                prev = dfs(prev.right)
                root.left = None
            return prev
        
        if root:
            dfs(root)
            